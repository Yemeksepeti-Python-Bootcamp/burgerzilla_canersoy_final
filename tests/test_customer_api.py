# import json
# from flask_jwt_extended import create_access_token

# from app import db
# from app.models.orders import Orders


# from tests.base import BaseCase

# def get_all_customer_orders(self,accestoken):
#     return self.client.get(
#         "/customers/orders",
#         headers={"Authorization": "Bearer " + accestoken},
#     )

# def post_new_customer_order(self,accestoken,order):
#     return self.client.post(
#         "/customers/orders",
#         data=json.dumps(order),
#         content_type="application/json",
#         headers={"Authorization": "Bearer " + accestoken},
#     )

# def get_customer_order_detail(self,accestoken,orderId):
#     return self.client.get(
#         f"/customers/orders/{orderId}",
#         headers={"Authorization": "Bearer " + accestoken},
#     )

# def get_customer_order_detail(self,accestoken,orderId):
#     return self.client.delete(
#         f"/customers/orders/{orderId}",
#         headers={"Authorization": "Bearer " + accestoken},
#     )

# def put_update_customer_order(self,accesstoken,id,itemId):
#     return self.client.put(
#         f"/customers/orders/{id}",
#         data=json.dumps(itemId),
#         content_type="application/json",
#         headers={"Authorization": "Bearer " + accesstoken},
#     )

# class TestCustomerEndpoints(BaseCase):
#     def get_all_customer_orders(self):
#         order = Orders(itemId=2,restaurantId=2)
#         db.session.add(order)
#         db.session.commit()
        
#         access_token = create_access_token(identity=1)

#         response = get_all_customer_orders(access_token)
#         orders = json.loads(response.data.decode())

#         self.assertTrue(response.status_code == 200)
#         self.assertTrue(orders["orders"]['itemId'] == 2)
#         self.assertTrue(orders["orders"]['restaurantId'] == 2)