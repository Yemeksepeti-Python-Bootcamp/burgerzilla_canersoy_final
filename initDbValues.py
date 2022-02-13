from app import app,db
from app.models.menu import Menu
from app.models.restaurants import Restaurants
from app.models.users import Users

"""
INSERT INTO users (type,name_surname,email)
values ('Customer','Uğur Özyalı','ugurozy@musteri.nett'),
('Customer','Ezel Özlüyalı','ezelozy@musteri.nett'),
('Restaurant','Ömer Kandor','omerk@restoran.nett'),
('Restaurant','Tunç Dimdal','tuncd@restoran.nett')
"""

"""
INSERT INTO restaurants (name,"userId")
values ('Dombili Burger',3),
('Dublemumble',4)
"""

"""
INSERT INTO menu (name,price,description,image,"restaurantId")
values ('Bombili',30,'Meşhur dombili burger, özel soslu, sarmısaklı ve soğanlı','x-txmt-filehandle://job/Preview/resource/dombili-dombili-burger.jpg',1),
('Duble peynirli',50,'Çift katlı, mozerella ve çedarla bezenmiş dombili burger','x-txmt-filehandle://job/Preview/resource/dombili-duble-peynirli.jpg',1),
('Aç doyuran',75,'Üç katlı, zeytin soslu,özel ketçap ve tatlı mayonezli burger ve patates','x-txmt-filehandle://job/Preview/resource/dombili-ac-doyuran.jpg',1),
('Tekkatlı',25,'Bol domatesli, özel muble soslu','x-txmt-filehandle://job/Preview/resource/dombili-dombili-burger.jpg',2),
('Dublemuble',45,'Çift katlı, beyaz peynir + kaşar peynir soslu, duble hamburger','x-txmt-filehandle://job/Preview/resource/dombili-duble-peynirli.jpg',2),
('Delüks',70,'Özel dublemuble burger, patates ve eritme peynirle birlikte','x-txmt-filehandle://job/Preview/resource/dombili-ac-doyuran.jpg',2)
"""
@app.cli.command("initDbValues")
def initDbValues():
    objects = [
    Users(type="Customer",name_surname="Uğur Özyalı",email="ugurozy@musteri.nett"),
    Users(type="Customer",name_surname="Ezel Özlüyalı",email="ezelozy@musteri.nett"),
    Users(type="Restaurant",name_surname="Ömer Kandor",email="omerk@restoran.nett"),
    Users(type="Restaurant",name_surname="Tunç Dimdal",email="tuncd@restoran.nett"),
    Restaurants(name="Dombili Burger",userId=3),
    Restaurants(name="Dublemumble",userId=4),
    Menu(name="Bombili",price=30,description="Meşhur dombili burger, özel soslu, sarmısaklı ve soğanlı",image="x-txmt-filehandle://job/Preview/resource/dombili1.jpg",restaurantId=1),
    Menu(name="Duble peynirli",price=50,description="Çift katlı, mozerella ve çedarla bezenmiş dombili burger",image="x-txmt-filehandle://job/Preview/resource/dombili2.jpg",restaurantId=1),
    Menu(name="Aç doyuran",price=75,description="Üç katlı, zeytin soslu,özel ketçap ve tatlı mayonezli burger ve patates",image="x-txmt-filehandle://job/Preview/resource/dombili3.jpg",restaurantId=1),
    Menu(name="Tekkatlı",price=25,description="Bol domatesli, özel muble soslu",image="x-txmt-filehandle://job/Preview/resource/dublemuble1.jpg",restaurantId=2),
    Menu(name="Dublemuble",price=45,description="Çift katlı, beyaz peynir + kaşar peynir soslu, duble hamburger",image="x-txmt-filehandle://job/Preview/resource/dublemuble2.jpg",restaurantId=2),
    Menu(name="Delüks",price=70,description="Özel dublemuble burger, patates ve eritme peynirle birlikte",image="x-txmt-filehandle://job/Preview/resource/dublemuble3.jpg",restaurantId=2)
    ]
    for obj in objects:
        db.session.add(obj)
    db.session.commit()
