from app import db

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(255),server_default="Customer")
    name_surname = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255),server_default="123")
    createdOn = db.Column(db.DateTime,server_default=db.func.now())
    status = db.Column(db.Integer,server_default="1") #1 is active 0 is inactive
    orders = db.relationship('Orders',backref='users',lazy='dynamic')
    restaurants = db.relationship('Restaurants',backref='users',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name_surname)