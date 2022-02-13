from flask_restx import fields 
from app import api 

user_model = api.model('User', 
{'id':fields.Integer(),
'type':fields.String(),
'name_surname':fields.String(),
'email':fields.String(),
'createdOn':fields.DateTime(),
'status':fields.Integer()})