from flask_restx import fields 
from app import api 

menu_model = api.model('Menu', 
{'itemId':fields.Integer(),
'name':fields.String(),
'price':fields.Float(),
'description':fields.String(),
'image':fields.String(),
'restaurantId':fields.Integer(),
'createdOn':fields.DateTime(),
'status':fields.Integer()})