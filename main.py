from classes_with_method import *
from datetime import datetime
from classes_with_method import shop
from fastapi import FastAPI
from typing import Optional
from scene import *




app = FastAPI()

@app.get("/")
def	root():
	return ({"msg":"Welcome to root path, there are nothing here, better specofic path  , for example , /products or /users"})

# example 127.0.0.1:58742/Products?name=Keychron
# example 127.0.0.1:58742/Products?in_type=Lips
@app.get("/Products")
def	products(name:Optional[str] = None, in_type:Optional[str] = None):
	return (product_cat.browse_product(name, in_type))

@app.get("/Products/{product_id}")
def	view_product(product_id : str):
	return (product_cat.view_product(product_id))

@app.get("/Users/{username}")
def	view_user(username : str):
	# need to check searching name is a guy who search or not ... but how?
	return (shop.get_user_by_username(username).get_user_detail())

@app.get("/Users/{username}/cart")
def	view_cart(username : str):
	# need to check searching name is a guy who search or not ... but how?
	return (shop.get_user_by_username(username).shopping_cart.show_cart())

@app.post("Products/{product_id}/add_to_cart")
def	add_to_cart(username, product_id, quantity):
	if (shop.get_user_by_username(username).shopping_cart.add_to_cart(product_cat.get_inst_product_by_id(product_id), quantity))
		return ("OK")
	return ("KO")

@app.post("/User/{username}/cart/checkout")
def	make_purchase(username):
	if (shop.get_user_by_username(username).make_purchase())
		return ("OK")
	return ("KO")


# @app.post("/users/{username}/cart/checkout")
# def make_purchase():	
# 	od = cart.new_order(order_id_gen,current_time,"thisIsAName")
# 	return (od.get_order_detail())



# od = cart.new_order(order_id_gen.generateID(),current_time,"thisIsAName")
# print(od.get_order_detail())

# for item in od.items:
# 	print(item.product.name)

# print()
# print(product_cat.browse_product(None,"Lips"))