# backend/app/utils/auth_utils.py
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def generate_token(user_id):
    return create_access_token(identity=user_id)

def verify_token():    
    return jwt_required()

def get_user_id():
    return get_jwt_identity()
