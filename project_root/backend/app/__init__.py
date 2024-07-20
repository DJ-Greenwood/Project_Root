from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from neo4j import GraphDatabase
from sqlalchemy import inspect
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
neo4j_driver = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize CORS
    CORS(app)
    
    db.init_app(app)
    jwt.init_app(app)

    global neo4j_driver
    neo4j_driver = GraphDatabase.driver(
        app.config['NEO4J_URI'],
        auth=(app.config['NEO4J_USER'], app.config['NEO4J_PASSWORD'])
    )

    from .routes import main, auth, data_ingestion, etl, ml_model, output
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(data_ingestion.bp, url_prefix='/data')
    app.register_blueprint(etl.bp, url_prefix='/etl')
    app.register_blueprint(ml_model.bp, url_prefix='/model')
    app.register_blueprint(output.bp, url_prefix='/output')

    @app.route('/auth/login', methods=['OPTIONS'])
    def auth_login_options():
        return '', 200

    with app.app_context():
        create_tables_if_not_exist()

    return app

def create_tables_if_not_exist():
    inspector = inspect(db.engine)
    if not inspector.has_table('user'):
        db.create_all()
