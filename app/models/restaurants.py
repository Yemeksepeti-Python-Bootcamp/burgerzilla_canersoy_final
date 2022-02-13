from app import db

class Restaurants(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    userId = db.Column(db.Integer, db.ForeignKey('users.id'),index=True)
    createdOn = db.Column(db.DateTime,server_default=db.func.now())
    status = db.Column(db.Integer,server_default="1") #1 is active 0 is inactive
    menu = db.relationship('Menu',backref='restaurants',lazy='dynamic')
    orders = db.relationship('Orders',backref='restaurants',lazy='dynamic')
        
    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)