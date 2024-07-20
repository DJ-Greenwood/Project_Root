# backend/app/routes/output.py
from flask import Blueprint, request, jsonify
from ..utils.neo4j_utils import neo4j_transaction
from ..utils.auth_utils import verify_token

bp = Blueprint('output', __name__)

@bp.route('/output', methods=['POST'])
@verify_token()
def create_output():
    data = request.get_json()
    
    @neo4j_transaction
    def create_output_node(tx, name, description, model_id, output_type):
        query = (
            "MATCH (model:MLModel) WHERE ID(model) = $model_id "
            "CREATE (output:Output {name: $name, description: $description, type: $output_type}) "
            "CREATE (model)-[:PRODUCES]->(output) "
            "RETURN output"
        )
        result = tx.run(query, name=name, description=description, model_id=int(model_id), output_type=output_type)
        return result.single()['output']

    output = create_output_node(data['name'], data['description'], data['model_id'], data['type'])
    return jsonify({"message": "Output created", "id": output.id}), 201

@bp.route('/output/<output_id>/data', methods=['POST'])
@verify_token()
def add_output_data(output_id):
    data = request.get_json()
    
    @neo4j_transaction
    def add_data_to_output(tx, output_id, data_value):
        query = (
            "MATCH (output:Output) WHERE ID(output) = $output_id "
            "CREATE (data:OutputData {value: $data_value, timestamp: datetime()}) "
            "CREATE (output)-[:HAS_DATA]->(data) "
            "RETURN data"
        )
        result = tx.run(query, output_id=int(output_id), data_value=data_value)
        return result.single()['data']

    output_data = add_data_to_output(output_id, data['value'])
    return jsonify({"message": "Output data added", "id": output_data.id}), 201

@bp.route('/output', methods=['GET'])
@verify_token()
def get_outputs():
    @neo4j_transaction
    def fetch_outputs(tx):
        query = (
            "MATCH (output:Output)<-[:PRODUCES]-(model:MLModel) "
            "OPTIONAL MATCH (output)-[:HAS_DATA]->(data:OutputData) "
            "RETURN output, model, collect(data) as data_points"
        )
        result = tx.run(query)
        return [{
            "output": record["output"],
            "model": record["model"],
            "data_points": record["data_points"]
        } for record in result]

    outputs = fetch_outputs()
    return jsonify(outputs), 200