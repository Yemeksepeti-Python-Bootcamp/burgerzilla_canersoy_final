# Burgerzilla

A REST-API micro-service enables transactions between customers and hamburger restaurants.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-Restx - restful API library.
3. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

## Requirements

Install with pip:

```
$ pip install -r requirements.txt
```

## Logging
```
The logger.py file includes function logEvent that allows all transactions to be logged into logs.txt file
```

## DB Schema
<img alt="DB_Schema.png" height="500" src="DB_Schema.png" width="500"/>

## Burgerzilla Application Structure 
```
burgerzilla_canersoy_final
├─ .gitignore
├─ DB_Schema.png
├─ Dockerfile
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ apimodels
│  │  ├─ menu.py
│  │  ├─ orders.py
│  │  ├─ restaurants.py
│  │  └─ users.py
│  ├─ models
│  │  ├─ menu.py
│  │  ├─ orders.py
│  │  ├─ restaurants.py
│  │  └─ users.py
│  └─ routes
│     ├─ customer.py
│     ├─ login.py
│     ├─ menu.py
│     └─ restaurant.py
├─ app.py
├─ boot.sh
├─ config.py
├─ docker-compose.yml
├─ initDbValues.py
├─ logger.py
├─ logs.txt
├─ requirements.txt
└─ tests
   ├─ base.py
   ├─ test_customer_api.py
   ├─ test_login_api.py
   ├─ test_menu_api.py
   └─ test_restaurant_api.py
```

## Swagger documentation page

```
http://127.0.0.1:5000/docs
```

## Dockerize
### Execute the following commands in order:

```
docker build -t burgerzilla:latest .
docker compose up --build web
```

## Predefined postgresql insert into commands:

```
INSERT INTO users (type,name_surname,email)
values ('Customer','Uğur Özyalı','ugurozy@musteri.nett'),('Customer','Ezel Özlüyalı','ezelozy@musteri.nett'),
('Restaurant','Ömer Kandor','omerk@restoran.nett'),('Restaurant','Tunç Dimdal','tuncd@restoran.nett')
```

```
INSERT INTO restaurants (name,"userId")
values ('Dombili Burger',3),('Dublemumble',4)
```

```
INSERT INTO menu (name,price,description,image,"restaurantId")
values ('Bombili',30,'Meşhur dombili burger, özel soslu, sarmısaklı ve soğanlı','x-txmt-filehandle://job/Preview/resource/dombili-dombili-burger.jpg',1),
('Duble peynirli',50,'Çift katlı, mozerella ve çedarla bezenmiş dombili burger','x-txmt-filehandle://job/Preview/resource/dombili-duble-peynirli.jpg',1),
('Aç doyuran',75,'Üç katlı, zeytin soslu,özel ketçap ve tatlı mayonezli burger ve patates','x-txmt-filehandle://job/Preview/resource/dombili-ac-doyuran.jpg',1),
('Tekkatlı',25,'Bol domatesli, özel muble soslu','x-txmt-filehandle://job/Preview/resource/dombili-dombili-burger.jpg',2),
('Dublemuble',45,'Çift katlı, beyaz peynir + kaşar peynir soslu, duble hamburger','x-txmt-filehandle://job/Preview/resource/dombili-duble-peynirli.jpg',2),
('Delüks',70,'Özel dublemuble burger, patates ve eritme peynirle birlikte','x-txmt-filehandle://job/Preview/resource/dombili-ac-doyuran.jpg',2)
```

<br/><br/>

# **While the app is running on docker, be sure to test the enpoints on URL http://localhost:80/**
```
Example: http://localhost:80/login
```

<br/><br/>

# Customer endpoints
## Login
Send a post request with email and password<br/>
POST http://127.0.0.1:5000/login

REQUEST
```json
{
    "email":"ugurozy@musteri.nett",
    "password":"123"
}
```
RESPONSE
```json
{
    "message": "Login succeeded!",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NDQ1Mzk2NiwianRpIjoiMWY4YmUyMzMtYmQzNi00MjJlLThmYTQtYTU1YTRjZTgwNmE2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjQ0NDUzOTY2LCJleHAiOjE2NDQ0NTQ4NjZ9.SNIrfQczFLHGp5rFK31GRRpnY6r-ZRwjBxQCZaBksHw"
}
```

## Current User
Returns the user id of the logged in user<br/>
GET http://127.0.0.1:5000/currentUser
RESPONSE
```json
{
    "logged_in_as": 1
}
```

## Create A New Customer Order
Create a new customer order with menu item id and restaurant id.<br/>
To order a single menu item, send JSON object alone<br/>
To order multiple menu items, send JSON object in a list<br/>
POST http://127.0.0.1:5000/customers/orders

REQUEST
```json
{
    "itemId":1,
    "restaurantId":1
}
```
RESPONSE
```json
{
    "order": {
        "id": 1,
        "orderId": "f9f2fe84-1c36-4ea0-82a9-7610ebfd9939",
        "itemId": 1,
        "userId": 1,
        "restaurantId": 1,
        "orderStatus": "Preparing",
        "createdOn": "2022-02-10T03:53:13.818894",
        "status": 1
    }
}
```

REQUEST
```json
[
    {
    "itemId":2,
    "restaurantId":1
    },
    {
    "itemId":3,
    "restaurantId":1
    }
]
```
RESPONSE
```json
{
    "order": [
        {
            "id": 2,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 2,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:54:19.168105",
            "status": 1
        },
        {
            "id": 3,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 3,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:54:19.171392",
            "status": 1
        }
    ]
}
```

## Get All Orders Of Customer
Returns all active orders of the customer<br/>
GET http://127.0.0.1:5000/customers/orders

RESPONSE
```json
{
    "orders": [
        {
            "id": 1,
            "orderId": "f9f2fe84-1c36-4ea0-82a9-7610ebfd9939",
            "itemId": 1,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:53:13.818894",
            "status": 1
        },
        {
            "id": 2,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 2,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:54:19.168105",
            "status": 1
        },
        {
            "id": 3,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 3,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:54:19.171392",
            "status": 1
        }
    ]
}
```

## Get Details Of A Customer Order
Returns details of a customer order<br/>
The orderId must be specified in the enpoint 
(not to be confused with the regular id!)<br/>
GET http://127.0.0.1:5000/customers/orders/string:orderId<br/>
Ex: http://127.0.0.1:5000/customers/orders/5ec60049-c688-4f3b-b783-2c072beb0885

RESPONSE
```json
{
    "order": [
        {
            "id": 2,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 2,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:54:19.168105",
            "status": 1
        },
        {
            "id": 3,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 3,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T03:54:19.171392",
            "status": 1
        }
    ]
}
```

## Cancel A Customer Order
Changes order status to 'Canceled by customer' and status to 0<br/>
DELETE http://127.0.0.1:5000/customers/orders/string:orderId<br/>
Ex: http://127.0.0.1:5000/customers/orders/5ec60049-c688-4f3b-b783-2c072beb0885

RESPONSE
```json
{
    "order": [
        {
            "id": 2,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 2,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Canceled by customer",
            "createdOn": "2022-02-10T03:54:19.168105",
            "status": 0
        },
        {
            "id": 3,
            "orderId": "5ec60049-c688-4f3b-b783-2c072beb0885",
            "itemId": 3,
            "userId": 1,
            "restaurantId": 1,
            "orderStatus": "Canceled by customer",
            "createdOn": "2022-02-10T03:54:19.171392",
            "status": 0
        }
    ]
}
```

## Update A Customer Order
Update a menu item in a customer order<br/>
The id (Orders.id) must be specified in the enpoint 
(not to be confused with the orderId!)<br/>
PUT http://127.0.0.1:5000/customers/orders/int:id<br/>
Ex: http://127.0.0.1:5000/customers/orders/1

REQUEST
```json
{
    "itemId":2
}
```
RESPONSE
```json
{
    "order": {
        "id": 1,
        "orderId": "f9f2fe84-1c36-4ea0-82a9-7610ebfd9939",
        "itemId": 2,
        "userId": 1,
        "restaurantId": 1,
        "orderStatus": "Preparing",
        "createdOn": "2022-02-10T03:53:13.818894",
        "status": 1
    }
}
```
<br/><br/>

# Restaurant endpoints
## Login
Send a post request with email and password<br/>
POST http://127.0.0.1:5000/login

REQUEST
```json
{
    "email":"tuncd@restoran.nett",
    "password":"123"
}
```
RESPONSE
```json
{
    "message": "Login succeeded!",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NDQ1NTU2NiwianRpIjoiYmZjODVjMzAtZWI1OS00NTJiLTkwMjgtM2E4NGI1MzMwZTdjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NCwibmJmIjoxNjQ0NDU1NTY2LCJleHAiOjE2NDQ0NTY0NjZ9.q1woYDMI5V8pCaW04kfygs9SAlJlZpRdEM3yPGZGCww"
}
```

## Current User
Returns the user id of the logged in user<br/>
GET http://127.0.0.1:5000/currentUser
RESPONSE
```json
{
    "logged_in_as": 4
}
```

## Get All Orders Of Restaurant
Returns all active orders of the restaurant<br/>
GET http://127.0.0.1:5000/restaurants/orders

RESPONSE
```json
{
    "orders": [
        {
            "id": 4,
            "orderId": "74bbadbd-d025-4b7e-9c00-0124d34190de",
            "itemId": 2,
            "userId": 1,
            "restaurantId": 2,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T04:15:01.026117",
            "status": 1
        },
        {
            "id": 5,
            "orderId": "74bbadbd-d025-4b7e-9c00-0124d34190de",
            "itemId": 3,
            "userId": 1,
            "restaurantId": 2,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T04:15:01.029692",
            "status": 1
        },
        {
            "id": 6,
            "orderId": "b13af964-af70-4dd1-9cce-42904239f869",
            "itemId": 1,
            "userId": 1,
            "restaurantId": 2,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T04:15:22.891258",
            "status": 1
        }
    ]
}
```

## Get Details Of A Customer Order
Returns details of a customer order<br/>
The orderId must be specified in the enpoint 
(not to be confused with the regular id!)<br/>
GET http://127.0.0.1:5000/restaurants/orders/string:orderId<br/>
Ex: http://127.0.0.1:5000/restaurants/orders/b13af964-af70-4dd1-9cce-42904239f869

RESPONSE
```json
{
    "order": [
        {
            "id": 6,
            "orderId": "b13af964-af70-4dd1-9cce-42904239f869",
            "itemId": 1,
            "userId": 1,
            "restaurantId": 2,
            "orderStatus": "Preparing",
            "createdOn": "2022-02-10T04:15:22.891258",
            "status": 1
        }
    ]
}
```

## Update A Customer Order Status
Change the order status of a customer order<br/>
The orderId must be specified in the enpoint 
(not to be confused with the regular id!)<br/>
PUT http://127.0.0.1:5000/restaurants/orders/string:orderId/string:status<br/>
Ex: http://127.0.0.1:5000/restaurants/orders/b13af964-af70-4dd1-9cce-42904239f869/cancel

RESPONSE
```json
{
    "order": [
        {
            "id": 6,
            "orderId": "b13af964-af70-4dd1-9cce-42904239f869",
            "itemId": 1,
            "userId": 1,
            "restaurantId": 2,
            "orderStatus": "Canceled by restaurant",
            "createdOn": "2022-02-10T04:15:22.891258",
            "status": 0
        }
    ]
}
```
<br/><br/>

# Menu endpoints
## View menu of restaurant
View all menu items in restaurant menu<br/>
GET http://127.0.0.1:5000/restaurants/menu

RESPONSE
```json
{
    "menu": [
        {
            "itemId": 4,
            "name": "Tekkatlı",
            "price": 25.0,
            "description": "Bol domatesli, özel muble soslu",
            "restaurantId": 2,
            "createdOn": "2022-02-10T03:45:44.591301",
            "status": 1
        },
        {
            "itemId": 5,
            "name": "Dublemuble",
            "price": 45.0,
            "description": "Çift katlı, beyaz peynir + kaşar peynir soslu, duble hamburger",
            "restaurantId": 2,
            "createdOn": "2022-02-10T03:45:44.591301",
            "status": 1
        },
        {
            "itemId": 6,
            "name": "Delüks",
            "price": 70.0,
            "description": "Özel dublemuble burger, patates ve eritme peynirle birlikte",
            "restaurantId": 2,
            "createdOn": "2022-02-10T03:45:44.591301",
            "status": 1
        }
    ]
}
```

## Add a new menu item
Add new menu item to restaurant menu<br/>
POST http://127.0.0.1:5000/restaurants/menu

REQUEST
```json
{
    "name":"Test Item",
    "price":100,
    "description":"Test item description"
}
```
RESPONSE
```json
{
    "menuItem": {
        "itemId": 7,
        "name": "Test Item",
        "price": 100.0,
        "description": "Test item description",
        "restaurantId": 2,
        "createdOn": "2022-02-10T04:27:53.472778",
        "status": 1
    }
}
```

## View a menu item
Get details of a menu item in restaurant menu<br/>
The menu item id must be specified in the enpoint<br/>
GET http://127.0.0.1:5000/restaurants/menu/int:itemId<br/>
Ex: http://127.0.0.1:5000/restaurants/menu/4

RESPONSE
```json
{
    "menuItem": {
        "itemId": 4,
        "name": "Tekkatlı",
        "price": 25.0,
        "description": "Bol domatesli, özel muble soslu",
        "restaurantId": 2,
        "createdOn": "2022-02-10T03:45:44.591301",
        "status": 1
    }
}
```

## Delete a menu item
Changes status of a menu item in restaurant menu to 0<br/>
The menu item id must be specified in the enpoint<br/>
DELETE http://127.0.0.1:5000/restaurants/menu/int:itemId<br/>
Ex: http://127.0.0.1:5000/restaurants/menu/7

RESPONSE
```json
{
    "menuItem": {
        "itemId": 7,
        "name": "Test Item",
        "price": 100.0,
        "description": "Test item description",
        "restaurantId": 2,
        "createdOn": "2022-02-10T04:27:53.472778",
        "status": 0
    }
}
```

## Update a menu item
Update name, price, description and/or image of a menu item in restaurant menu<br/>
The menu item id must be specified in the enpoint<br/>
PUT http://127.0.0.1:5000/restaurants/menu/int:itemId<br/>
Ex: http://127.0.0.1:5000/restaurants/menu/4

REQUEST
```json
{
    "name":"Duble baya peynirli",
    "price":40,
    "description":"Baya iyi burger"
}
```
RESPONSE
```json
{
    "menuItem": {
        "itemId": 4,
        "name": "Duble baya peynirli",
        "price": 40.0,
        "description": "Baya iyi burger",
        "restaurantId": 2,
        "createdOn": "2022-02-10T03:45:44.591301",
        "status": 1
    }
}
```