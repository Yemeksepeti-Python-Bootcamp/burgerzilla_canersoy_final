from flask import request
from app import api,db
from flask_restx import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
import uuid
from logger import logEvent

from app.apimodels.orders import order_model

from app.models.orders import Orders
from app.models.users import Users

#Endpoint used to get all orders of customer
#Or post a new order for customer
@api.route('/customers/orders')
class CustomerOrders(Resource):
    @api.marshal_with(order_model,code=200,envelope='orders')
    @jwt_required()
    def get(self):
        '''Get all orders of customer'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get active (status=1) orders of user
            orders = Orders.query.filter(Orders.userId==user.id,Orders.status==1).all()
            logEvent(f"Customer with id {user.id} viewed all of his/her orders.")
            return orders
        except Exception as e:
            logEvent(f"Received an error when customer with id {user.id} tried to view all of his/her orders: {e}")
            return {"message":e},400

    @api.marshal_with(order_model,code=201,envelope='order')
    @api.doc(params={'itemId':'Item Id','restaurantId':'Restaurant Id'})
    @jwt_required()
    def post(self):
        '''Create a new order for customer'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            json_data = request.get_json()
            #generate an unique orderId
            orderId = uuid.uuid4()
            if type(json_data) is list and len(json_data) > 0:
                #init an empty array which will be used to handle response
                #if multiple menu items are added to the order
                new_array_order = []
                #loop json_data list that contains multiple menu items
                for i in json_data:
                    itemId = i['itemId']
                    restaurantId = i['restaurantId']
                    if itemId and restaurantId:
                        new_order = Orders(orderId=orderId,userId=user.id,itemId=itemId,restaurantId=restaurantId)
                        #add menu item to new_array_order
                        new_array_order.append(new_order)
                        db.session.add(new_order)
                        db.session.commit()
                    else:
                        logEvent(f"Customer with id {user.id} failed to create an order due to empty itemId and/or restaurantId field.")
                        return {"message":"itemId and restaurantId fields cannot be empty!"},400
                logEvent(f"Customer with id {user.id} created a new order with itemIds {str([v['itemId'] for v in json_data])} from restaurant(s) {str([v['restaurantId'] for v in json_data])}")
                return new_array_order
            else:
                #handle request if only one menu item is being ordered
                itemId = json_data.get("itemId")
                restaurantId = json_data.get("restaurantId")
                new_order = Orders(orderId=orderId,userId=user.id,itemId=itemId,restaurantId=restaurantId)
                db.session.add(new_order)
                db.session.commit()
                logEvent(f"Customer with id {user.id} created a new order with itemId {itemId} from restaurant {restaurantId}")
                return new_order
        except Exception as e:
            logEvent(f"Received an error when customer with id {user.id} tried to create an order: {e}")
            return {"message":e},400

#Enpoint used to get details of an order
#Or cancel an order of customer
#The <string:orderId> parameter is the orderId column
#of the Order table 
@api.route('/customers/orders/<string:orderId>')
class CustomerOrderItem(Resource):
    @api.marshal_with(order_model,code=200,envelope='order')
    @jwt_required()
    def get(self,orderId):
        '''Get order details'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            order = Orders.query.filter(Orders.userId==user.id,Orders.orderId==orderId).all()
            logEvent(f"Customer with id {user.id} viewed details of his/her order with orderId {orderId}")
            return order
        except Exception as e:
            logEvent(f"Received an error when customer with id {user.id} tried to view details of his/her order with orderId {orderId}: {e}")
            return {"message":e},400
    
    @api.marshal_with(order_model,code=200,envelope='order')
    @jwt_required()
    def delete(self,orderId):
        '''Cancel an order'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            order = Orders.query.filter(Orders.userId==user.id,Orders.orderId==orderId).all()
            for i in order:
                i.orderStatus = "Canceled by customer"
                i.status = 0
                db.session.commit()
            logEvent(f"Customer with id {user.id} canceled his/her order with orderId {orderId}")
            return order 
        except Exception as e:
            logEvent(f"Received an error when customer with id {user.id} tried to cancel his/her order with orderId {orderId}: {e}")
            return {"message":e},400

#Endpoint used to update a menu item in order
#The <int:id>' parameter is the id column of the Order table,
#Not to be confused with orderId!
@api.route('/customers/orders/<int:id>')
class CustomerOrderItemUpdate(Resource):
    @api.marshal_with(order_model,code=200,envelope='order')
    @api.doc(params={'itemId':'Item Id'})
    @jwt_required()
    def put(self,id):
        '''Update a menu item of order'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            order = Orders.query.filter(Orders.userId==user.id,Orders.id==id).first()
            json_data = request.get_json()
            itemId = json_data.get('itemId')
            if itemId:
                order.itemId = json_data.get('itemId')
                db.session.commit()
                logEvent(f"Customer with id {user.id} updated itemId as {itemId} in his/her order with id of order as {id}")
                return order
            else:
                logEvent(f"Customer with id {user.id} failed to update an itemId of his/her order with id of order {id} due to empty itemId field.")
                return {"message":"itemId field cannot be empty!"},400
        except Exception as e:
            logEvent(f"Received an error when customer with id {user.id} tried to update an itemId of his/her order with id of order as {id}: {e}")
            return {"message":e},400

