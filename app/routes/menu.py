from os import name
from flask import request
from app import api,db
from flask_restx import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from logger import logEvent

from app.apimodels.menu import menu_model

from app.models.menu import Menu
from app.models.restaurants import Restaurants
from app.models.users import Users

#Endpoint used to get all menu items of restaurant
#Or add a new menu item to restaurant menu
@api.route('/restaurants/menu')
class RestaurantMenu(Resource):
    @api.marshal_list_with(menu_model,code=200,envelope='menu')
    @jwt_required()
    def get(self):
        '''Get all menu items in restaurant menu'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter(Restaurants.userId==user.id).first()
            menuItems = Menu.query.filter(Menu.restaurantId==restaurant.id,Menu.status==1).all()
            logEvent(f"Restaurant with id {restaurant.id} viewed all of its menu items.")
            return menuItems
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to view all of its menu items: {e}")
            return {"message":e},400
    
    @api.marshal_with(menu_model,code=201,envelope='menuItem')
    @jwt_required()
    def post(self):
        '''Add a new menu item into restaurant menu'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter_by(userId=user.id).first()
            json_data = request.get_json()
            name = json_data.get("name")
            price = json_data.get("price")
            description = json_data.get("description")
            image = json_data.get("image")
            if name and price and description:
                menuItem = Menu(name=name,price=price,description=description,image=image,restaurantId=restaurant.id)
                db.session.add(menuItem)
                db.session.commit()
                logEvent(f"Restaurant with id {restaurant.id} added a new menu item to its menu: {name},{price},{description}.")
                return menuItem
            else:
                logEvent(f"Restaurant with id {restaurant.id} failed to add a new menu item to its menu due to empty name, price and/or description field.")
                return {"message":"name, price and description fields cannot be empty!"},400
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to add a new menu item to its menu: {e}")
            return {"message":e},400

#Endpoint used to get, delete or update a menu item
#The <int:menuItemId> parameter is the itemId column
#of the Menu table
@api.route('/restaurants/menu/<int:menuItemId>')
class RestaurantMenuItem(Resource):
    @api.marshal_with(menu_model,code=200,envelope='menuItem')
    @jwt_required()
    def get(self,menuItemId):
        try:
            '''Get details of a menu item in restaurant menu'''
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter_by(userId=user.id).first()
            menuItem = Menu.query.filter(Menu.restaurantId==restaurant.id,Menu.itemId==menuItemId).first()
            logEvent(f"Restaurant with id {restaurant.id} viewed details of its menu item with menu itemId {menuItemId}.")
            return menuItem
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to view details of its menu item with menu itemId {menuItemId}: {e}")
            return {"message":e},400
    
    @api.marshal_with(menu_model,code=200,envelope='menuItem')
    @jwt_required()
    def delete(self,menuItemId):
        '''Delete a menu item in restaurant menu'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter_by(userId=user.id).first()
            menuItem = Menu.query.filter(Menu.restaurantId==restaurant.id,Menu.itemId==menuItemId).first()
            menuItem.status = 0
            db.session.commit()
            logEvent(f"Restaurant with id {restaurant.id} deleted its menu item with menu itemId {menuItemId}.")
            return menuItem
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to delete its menu item with menu itemId {menuItemId}: {e}")
            return {"message":e},400
        
    @api.marshal_with(menu_model,code=200,envelope='menuItem')
    @jwt_required()
    def put(self,menuItemId):
        '''Update a menu item in restaurant menu'''
        try:
            #get user obj by id received from JWT token of logged in user
            user = Users.query.filter_by(id=get_jwt_identity()).first()
            #get restaurant obj by matching the user.Id with Restaurants.userId
            restaurant = Restaurants.query.filter_by(userId=user.id).first()
            menuItem = Menu.query.filter(Menu.restaurantId==restaurant.id,Menu.itemId==menuItemId).first()
            json_data = request.get_json()
            if json_data.get("name"):
                menuItem.name = json_data.get("name")
                logEvent(f"Restaurant with id {restaurant.id} changed 'name' of menu itemId {menuItemId}")
            if json_data.get("price"):
                menuItem.price = json_data.get("price")
                logEvent(f"Restaurant with id {restaurant.id} changed 'price' of menu itemId {menuItemId}")
            if json_data.get("description"):
                menuItem.description = json_data.get("description")
                logEvent(f"Restaurant with id {restaurant.id} changed 'description' of menu itemId {menuItemId}")
            if json_data.get("image"):
                menuItem.restaurant_id = json_data.get("image")
                logEvent(f"Restaurant with id {restaurant.id} changed 'image' of menu itemId {menuItemId}")
            db.session.commit()
            return menuItem
        except Exception as e:
            logEvent(f"Received an error when restaurant with id {restaurant.id} tried to update its menu item with menu itemId {menuItemId}: {e}")
            return {"message":e},400