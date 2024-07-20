# backend/app/utils/neo4j_utils.py
from flask import current_app
from neo4j import GraphDatabase

def neo4j_transaction(func):
    def wrapper(*args, **kwargs):
        with current_app.neo4j_driver.session() as session:
            return session.write_transaction(func, *args, **kwargs)
    return wrapper