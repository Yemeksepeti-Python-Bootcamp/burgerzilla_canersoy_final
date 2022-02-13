from app import api,db
from flask_restx import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from logger import logEvent

from app.apimodels.orders import order_model

from app.models.orders import Orders
from app.models.restaurants import Restaurants
from app.models.users import Users

#Endpoint used to get all orders of restaurant
@api.route('/restaurants/orders')
class RestaurantOrders(Resource):
    @api.marshal_list_with(order_model,code=200,envelope='orders')
    @jwt_required()
    def get(self):
        '''Get all orders of restaurant'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter(Restaurants.userId==user.id).first()
            #Here the orders are put in a queue by the following query:
            #order_by(Orders.createdOn.asc())
            orders = Orders.query.filter(Orders.restaurantId==restaurant.id,Orders.status==1).order_by(Orders.createdOn.asc()).all()
            logEvent(f"Restaurant with id {restaurant.id} viewed all of its orders.")
            return orders
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to view all of its orders: {e}")
            return {"message":e},400

#Enpoint used to get details of an order
#The <string:orderId> parameter is the orderId column
#of the Order table 
@api.route('/restaurants/orders/<string:orderId>')
class RestaurantOrderItem(Resource):
    @api.marshal_with(order_model,code=200,envelope='order')
    @jwt_required()
    def get(self,orderId):
        '''Get order details by order id'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter_by(userId=user.id).first()
            order = Orders.query.filter(Orders.orderId==orderId,Orders.restaurantId==restaurant.id).all()
            logEvent(f"Restaurant with id {restaurant.id} viewed details of its order with orderId {orderId}")
            return order
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to view details of his/her order with orderId {orderId}: {e}")
            return {"message":e},400

#Endpoint used to change the order status
#The <string:orderId> parameter is the orderId column
#of the Order table 
#The <string:status> parameter must be one of the following:
#preparing, onway, delivered, cancel
@api.route('/restaurants/orders/<string:orderId>/<string:status>')
class RestaurantOrderItemStatus(Resource):
    @api.marshal_with(order_model,code=200,envelope='order')
    @jwt_required()
    def put(self,orderId,status):
        '''Change status of an order to preparing, onway, delivered or cancel'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter_by(userId=user.id).first()
            order = Orders.query.filter(Orders.orderId==orderId,Orders.restaurantId==restaurant.id).all()
            if status not in ["preparing","onway","delivered","cancel"]:
                logEvent(f"Restaurant with id {user.id} failed to update the status of orderId {orderId} due to wrong status code.")
                return {"message":"Status must be equal to one of the following: 'preparing','onway','delivered' or 'cancel'"},400
            else:
                for i in order: 
                    if status == "preparing":
                        i.orderStatus = "Preparing"
                        logEvent(f"Restaurant with id {restaurant.id} changed order status of {orderId} to 'preparing'")
                    if status == "onway":
                        i.orderStatus = "On way"
                        logEvent(f"Restaurant with id {restaurant.id} changed order status of {orderId} to 'onway'")
                    if status == "delivered":
                        i.orderStatus = "Delivered"
                        i.status = 0 #set order inactive
                        logEvent(f"Restaurant with id {restaurant.id} changed order status of {orderId} to 'delivered'")
                    if status == "cancel":
                        i.orderStatus = "Canceled by restaurant"
                        i.status = 0 #set order inactive
                        logEvent(f"Restaurant with id {restaurant.id} changed order status of {orderId} to 'cancel'")
                db.session.commit()
                return order
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to change status of its order with orderId {orderId}: {e}")
            return {"message":e},400