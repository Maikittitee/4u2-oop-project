#from typing import Union
from fastapi import FastAPI

class Shop:
	def __init__(self):
		self.product_catalog = [] #AGRET ProductCatalog
		self.users = [] #AGGRESION User
		self.promotions = [] # AGGRESTION Promotion

shop = Shop()

class User:
	def __init__ (self, user_id, email, name):
		self.user_id = user_id
		self.email = email
		self.name = name
		self.account = None # Compostion Account ????

class Account:
	def __init__ (self, email, password):
		self.email = email
		self.password = password

class Admin(User):
	def __init__ (self, salary, shop):
		self.salary = salary
		self.shop = shop # Association (manage) Shop

class Customer(User):
	def __init__ (self):
		User.__init__(self,"1","email","Jiwa")
		# self.shopping_cart = ShoppingCart('SC' + user_id) # Association ShoppingCart 

class Guest(Customer):
	def	__init__ (self):
		pass

class AuthenticationUser(Customer):
	def	__init__ (self, address):
		Customer.__init__(self)
		self.address = address
		self.order = [] # Aggretion Order

	def return_user_detail(self):
		
		view_user_dict = {
			"user_id" : self.user_id,
			"email" : self.email,
			"name" : self.name,
			"address" : self.address,

		}
		return (view_user_dict)


user_3 = AuthenticationUser("sssssss")
user_3.user_id = "1"
user_3.email = "haha@gmail.com"
user_3.name = "6dsfhifhr"
user_3.address = "sygifkmsl"
shop.users.append(user_3)

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:str):
    for user in shop.users:
        if (user.user_id == user_id):
            return (user.return_user_detail())


print(user_3.return_user_detail())