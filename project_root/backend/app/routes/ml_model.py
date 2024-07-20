# backend/app/routes/ml_model.py
from flask import Blueprint, request, jsonify
from ..utils.neo4j_utils import neo4j_transaction
from ..utils.auth_utils import verify_token

bp = Blueprint('ml_model', __name__)

@bp.route('/model', methods=['POST'])
@verify_token()
def create_model():
    data = request.get_json()
    
    @neo4j_transaction
    def create_model_node(tx, name, version, description, input_features):
        query = (
            "CREATE (model:MLModel {name: $name, version: $version, description: $description}) "
            "WITH model "
            "UNWIND $input_features AS feature "
            "MERGE (f:Feature {name: feature}) "
            "CREATE (model)-[:USES_FEATURE]->(f) "
            "RETURN model"
        )
        result = tx.run(query, name=name, version=version, description=description, input_features=input_features)
        return result.single()['model']

    model = create_model_node(data['name'], data['version'], data['description'], data['input_features'])
    return jsonify({"message": "Model created", "id": model.id}), 201

@bp.route('/model/<model_id>/metric', methods=['POST'])
@verify_token()
def add_model_metric(model_id):
    data = request.get_json()
    
    @neo4j_transaction
    def add_metric_to_model(tx, model_id, metric_name, metric_value):
        query = (
            "MATCH (model:MLModel) WHERE ID(model) = $model_id "
            "CREATE (metric:Metric {name: $metric_name, value: $metric_value}) "
            "CREATE (model)-[:HAS_METRIC]->(metric) "
            "RETURN metric"
        )
        result = tx.run(query, model_id=int(model_id), metric_name=metric_name, metric_value=metric_value)
        return result.single()['metric']

    metric = add_metric_to_model(model_id, data['name'], data['value'])
    return jsonify({"message": "Model metric added", "id": metric.id}), 201

@bp.route('/model', methods=['GET'])
@verify_token()
def get_models():
    @neo4j_transaction
    def fetch_models(tx):
        query = (
            "MATCH (model:MLModel) "
            "OPTIONAL MATCH (model)-[:USES_FEATURE]->(feature:Feature) "
            "OPTIONAL MATCH (model)-[:HAS_METRIC]->(metric:Metric) "
            "RETURN model, collect(distinct feature) as features, collect(metric) as metrics"
        )
        result = tx.run(query)
        return [{
            "model": record["model"],
            "features": record["features"],
            "metrics": record["metrics"]
        } for record in result]

    models = fetch_models()
    return jsonify(models), 200