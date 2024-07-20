# backend/app/routes/data_ingestion.py
from flask import Blueprint, request, jsonify
from ..utils.neo4j_utils import neo4j_transaction
from ..utils.auth_utils import verify_token

bp = Blueprint('data_ingestion', __name__)

@bp.route('/ingest', methods=['POST'])
@verify_token()
def ingest_data():
    data = request.get_json()
    
    @neo4j_transaction
    def create_data_source(tx, name, type):
        query = (
            "CREATE (ds:DataSource {name: $name, type: $type}) "
            "RETURN ds"
        )
        result = tx.run(query, name=name, type=type)
        return result.single()['ds']

    data_source = create_data_source(data['name'], data['type'])
    return jsonify({"message": "Data source created", "id": data_source.id}), 201
