from flask import request
from app import api
from flask_restx import Resource
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
from logger import logEvent

from app.models.users import Users

#Login by email and password, get JWT token if successful, return 404 if failed
@api.route('/login')
class Login(Resource):
    @api.doc(params={'email':'Email address of user','password':'Password of user'})
    @api.response(200,'Login succeeded!')
    def post(self):
        '''Login by email and password'''
        try:
            email = request.json['email']
            password = request.json['password']
            user = Users.query.filter_by(email=email,password=password).first()
            if user:
                access_token = create_access_token(identity=user.id)
                logEvent(f"User successfully logged in with email {email}")
                return {"message":"Login succeeded!","access_token":access_token},200
            else:
                logEvent(f"User login failed due to bad email or password. Email: {email}")
                return {"message":"Bad email or password"},401
        except Exception as e:
            logEvent(f"Error during login {e}")
            return {"message":e},400

#View the userId of logged in user
@api.route('/currentUser')
class CurrentUser(Resource):
    @api.response(200,'logged_in_as')
    @jwt_required()
    def get(self):
        '''View the current user'''
        try:
            current_user = get_jwt_identity()
            logEvent(f"Current user: {current_user}")
            return {"logged_in_as":current_user},200
        except Exception as e:
            logEvent(f"Error in currentUser endpoint: {e}")
            return {"message":e},400