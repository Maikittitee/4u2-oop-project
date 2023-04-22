from classes_with_method import *
from datetime import datetime
from classes_with_method import shop
from fastapi import FastAPI
from typing import Optional
from scene import *
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

@app.get("/")
def	root():
	return ({"msg":"Welcome to root path, there are nothing here, better give a specific path  , for example , /Products or /Users"})

# example 127.0.0.1:58742/Products?name=Keychron
# example 127.0.0.1:58742/Products?in_type=Lips
@app.get("/Products")
def	products(name:Optional[str] = None, in_type:Optional[str] = None):
	return (product_cat.browse_product(name, in_type))

@app.get("/Products/{product_id}")
def	view_product(product_id : str):
	return (product_cat.view_product(product_id))

@app.post("/Users/{username}")
def	view_user_detail(username : str):
	# need to check searching name is a guy who search or not ... but how? -> Ohm said it's FRONTEND problem so yeah im not gonna do it.
	return (shop.get_user_by_username(username))

@app.get("/Users/{username}/cart")
def	view_cart(username : str):
	# need to check searching name is a guy who search or not ... but how? -> im won't do this one neither.
	return (shop.get_user_by_username(username).shopping_cart.show_cart())

@app.add("/Products/{product_id}/add_to_cart")
def	add_to_cart(username:str, product_id:str, quantity:int):
	ret = shop.get_user_by_username(username).shopping_cart.add_to_cart(product_cat.get_inst_product_by_id(product_id), quantity)
	if (ret):
		return (ret)
	return ("KO")

@app.post("/Users/{username}/cart/checkout")
def	make_purchase(username:str, address:str = None):
	user = shop.get_user_by_username(username)
	if (address == None):
		address = user.address
	if (user.make_purchase(address)):
		return ("OK")
	return ("KO")

@app.get("/Auth/login")
def	login(username: str, password: str):
	user = User(0)
	if (user.login(username, password)):
		return (username)
	return ("KO")

@app.post("/Auth/register")
def	register(username:str, email:str, password:str):
	guest = Guest()
	if (guest.register(username, email, password)):
		return (username)
	return ("KO")

@app.post("Auth/logout")
def	logout(username : str):
	if (shop.get_user_by_username(username).logout()):
		return ("OK")
	return ("KO")

@app.post("/Users/{username}/orders")
def	get_orders(username):
	return (shop.get_user_by_username(username).order)

@app.post("/Users/{username}/confirm_payment")
def	confirm_payment(order_id, username, amount):
	order = shop.get_user_by_username(username).get_order_by_id(order_id)
	if (not order):
		return ("KO")
	if (order.confirm_payment(amount)):
		return ("OK")
	return ("KO")

@app.post("/feat/orders")
def	view_order(email, order_id):
	if (shop.get_user_by_email(email).get_order_by_id(order_id)):
		return ("OK")
	return ("KO")

@app.post("/users/{username}/edit")
def	change_info():
	pass

