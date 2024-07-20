# backend/app/models/user.py
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

roles = ['user', 'admin']

class User(db.Model):
    """
    User model for authentication and authorization.
    
    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password_hash (str): The hashed password of the user.
        role (str): The role of the user (e.g., 'user', 'admin').
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64), default='user')

    def set_password(self, password):
        """
        Set the hashed password for the user.
        
        Args:
            password (str): The plain text password to be hashed.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the user's hashed password.
        
        Args:
            password (str): The plain text password to check.
        
        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return check_password_hash(self.password_hash, password)
    
    def select_role(self, role):
        """
        Select a role for the user.
        
        Args:
            role (str): The role to be assigned to the user.
        """
        if role in roles:
            self.role = role
        else:
            raise ValueError("Invalid role")
        

        
