from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config 
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app,doc="/docs",title="Burgerzilla APIs",description="Burgerzilla API descriptions",version="1.0")
jwt = JWTManager(app)

from app.routes.customer import CustomerOrders,CustomerOrderItem
from app.routes.login import Login,CurrentUser
from app.routes.menu import RestaurantMenu,RestaurantMenuItem
from app.routes.restaurant import RestaurantOrders,RestaurantOrderItem,RestaurantOrderItemStatus
from app.apimodels.menu import menu_model
from app.apimodels.orders import order_model
from app.apimodels.restaurants import restaurant_model
from app.apimodels.users import user_model
from app.models.menu import Menu
from app.models.orders import Orders
from app.models.restaurants import Restaurants
from app.models.users import Users

from initDbValues import initDbValues

import click

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run unit test """
    import unittest

    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests',pattern='test*.py')

    result =  unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1