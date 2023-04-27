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

@app.get("/Users/{username}")
def	view_user_detail(username : str):
	# need to check searching name is a guy who search or not ... but how? -> Ohm said it's FRONTEND problem so yeah im not gonna do it.
	print(shop.users)
	if (shop.get_user_by_username(username)):
		return (shop.get_user_by_username(username).get_user_detail())
	return ("KO")
	# return ("H)

@app.get("/Users/{username}/cart")
def	view_cart(username : str):
	# need to check searching name is a guy who search or not ... but how? -> im won't do this one neither.
	return (shop.get_user_by_username(username).shopping_cart.show_cart())

@app.get("/Products/{product_id}/add_to_cart")
def	add_to_cart(username:str, product_id:str, quantity:int):
	ret = shop.get_user_by_username(username).shopping_cart.add_to_cart(product_cat.get_inst_product_by_id(product_id), quantity)
	if (ret):
		return (ret)
	return ("KO")

@app.post("/Users/{username}/cart/checkout")
def	make_purchase(username:str, address_index:int):
	user = shop.get_user_by_username(username)
	if (user.make_purchase(user.address[address_index])):
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
	new = guest.register(username, email, password) 
	if (new):
		shop.users.append(new)
		return (new.name)
	return ("KO")

@app.post("/Auth/logout")
def	logout(username : str):
	if (shop.get_user_by_username(username).logout()):
		return ("OK")
	return ("KO")

@app.post("/Users/{username}/orders")
def	get_orders(username):
	print(shop.get_user_by_username(username).order)
	return (shop.get_user_by_username(username).get_user_order())

@app.post("/Users/{username}/confirm_payment")
def	confirm_payment(order_id, username, amount:int):
	order = shop.get_user_by_username(username).get_order_by_id(order_id)
	if (not order):
		return ("KO")
	if (order.confirm_payment(amount)):
		return ("OK")
	return ("KO")

@app.post("/feat/orders")
def	view_order(email, order_id):
	ret = shop.get_user_by_email(email).get_order_by_id(order_id).get_order_detail()
	if (ret):
		return (ret)
	return ("KO")

@app.post("/users/{username}/editinfo")
def	change_info(username, new_name, new_tel):
	user = shop.get_user_by_username(username)
	user.name = new_name
	user.tel = new_tel

@app.post("/users/{username}/add_address")
def	add_address(name, address, tel, username, type:int = 0):
	user = shop.get_user_by_username(username)
	if (type == 1):
		addr = ShippingAddress(name, address, tel)
	elif (type == 2):
		addr = TaxInvoiceAddress(name, address, tel)
	else:
		return ("KO")
	user.address.append(addr)
	return ("OK")

@app.delete("/users/{username}/del_address")
def	del_address(address_index:int, username):
	user = shop.get_user_by_username(username)
	user.address.pop(address_index)
	return ("OK")

@app.post("/users/{username}/change_password")
def	change_pass(new_pass, username):
	user = shop.get_user_by_username(username)
	user.account.password = new_pass
	return ("OK")

# ADMIN SIDE API 

@app.post("/admin/login")
def	admin_login(username:str, password:str):
	user = User(0)
	if (user.login(username, password, 1)):
		return (username)
	return ("KO")

@app.post("/admin/add_new_admin")
def	add_new_admin(name, salary:int, username, email, password):
	new_admin = Admin(name, salary, username, email, password)
	if (new_admin.register(username, email)):
		return (username)
	return ("KO")

@app.post("/admin/add_product")
def	add_product(name, price:int, specify, stock:int, description, detail, p_type:str):
	product_cat.add_product(name, price, specify, stock, description, detail, p_type)
	return ("OK")


