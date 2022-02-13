from app import db

class Orders(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    orderId = db.Column(db.String(255),index=True)
    userId = db.Column(db.Integer,db.ForeignKey('users.id'),index=True)
    itemId = db.Column(db.Integer,db.ForeignKey('menu.itemId'),index=True)
    restaurantId = db.Column(db.Integer, db.ForeignKey('restaurants.id'),index=True)
    orderStatus = db.Column(db.String(255),default="New")
    createdOn = db.Column(db.DateTime,server_default=db.func.now())
    status = db.Column(db.Integer,server_default="1") #1 is active 0 is inactive
        
    def __repr__(self):
        return '<Order id {}>'.format(self.orderId)