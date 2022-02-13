import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import TestingConfig
from app import db
from flask_jwt_extended import JWTManager

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    jwt = JWTManager(app)
    return app

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
