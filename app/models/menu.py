from app import db

class Menu(db.Model):
    itemId = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Numeric)
    description = db.Column(db.String(255))
    image = db.Column(db.String)
    restaurantId = db.Column(db.Integer,db.ForeignKey('restaurants.id'),index=True)
    createdOn = db.Column(db.DateTime,server_default=db.func.now())
    status = db.Column(db.Integer,server_default="1") #1 is active 0 is inactive
    orders = db.relationship('Orders',backref='menu',lazy='dynamic')
        
    def __repr__(self):
        return '<Menu of restaurant id {}>'.format(self.restaurantId)