from flask_restx import fields 
from app import api 

restaurant_model = api.model('Restaurant', 
{'id':fields.Integer(),
'name':fields.String(),
'userId':fields.Integer(),
'createdOn':fields.DateTime(),
'status':fields.Integer()})