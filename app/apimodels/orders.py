from flask_restx import fields 
from app import api 

order_model = api.model('Order', 
{'id':fields.Integer(),
'orderId':fields.String(),
'itemId':fields.Integer(),
'userId':fields.Integer(),
'restaurantId':fields.Integer(),
'orderStatus':fields.String(),
'createdOn':fields.DateTime(),
'status':fields.Integer()})