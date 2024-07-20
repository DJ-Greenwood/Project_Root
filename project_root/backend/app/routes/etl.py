# backend/app/routes/etl.py
from flask import Blueprint, request, jsonify
from ..utils.neo4j_utils import neo4j_transaction
from ..utils.auth_utils import verify_token

bp = Blueprint('etl', __name__)

@bp.route('/etl', methods=['POST'])
@verify_token()
def create_etl_process():
    data = request.get_json()
    
    @neo4j_transaction
    def create_etl_node(tx, name, description, input_sources):
        query = (
            "CREATE (etl:ETLProcess {name: $name, description: $description}) "
            "WITH etl "
            "UNWIND $input_sources AS source "
            "MATCH (ds:DataSource {name: source}) "
            "CREATE (ds)-[:INGESTED_BY]->(etl) "
            "RETURN etl"
        )
        result = tx.run(query, name=name, description=description, input_sources=input_sources)
        return result.single()['etl']

    etl_process = create_etl_node(data['name'], data['description'], data['input_sources'])
    return jsonify({"message": "ETL process created", "id": etl_process.id}), 201

@bp.route('/etl/<etl_id>/step', methods=['POST'])
@verify_token()
def add_etl_step(etl_id):
    data = request.get_json()
    
    @neo4j_transaction
    def add_step_to_etl(tx, etl_id, step_name, step_description):
        query = (
            "MATCH (etl:ETLProcess) WHERE ID(etl) = $etl_id "
            "CREATE (step:ETLStep {name: $step_name, description: $step_description}) "
            "CREATE (etl)-[:HAS_STEP]->(step) "
            "RETURN step"
        )
        result = tx.run(query, etl_id=int(etl_id), step_name=step_name, step_description=step_description)
        return result.single()['step']

    etl_step = add_step_to_etl(etl_id, data['name'], data['description'])
    return jsonify({"message": "ETL step added", "id": etl_step.id}), 201

@bp.route('/etl', methods=['GET'])
@verify_token()
def get_etl_processes():
    @neo4j_transaction
    def fetch_etl_processes(tx):
        query = (
            "MATCH (etl:ETLProcess) "
            "OPTIONAL MATCH (etl)-[:HAS_STEP]->(step:ETLStep) "
            "RETURN etl, collect(step) as steps"
        )
        result = tx.run(query)
        return [{"etl": record["etl"], "steps": record["steps"]} for record in result]

    etl_processes = fetch_etl_processes()
    return jsonify(etl_processes), 200