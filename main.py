from classes_with_method import *
from datetime import datetime
from classes_with_method import shop
from fastapi import FastAPI, APIRouter
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

customer = APIRouter()
admin = APIRouter()

@app.get("/")
async def	root():
	return ({"msg":"Welcome to root path, there are nothing here, better give a specific path  , for example , /Products or /Users"})

# example 127.0.0.1:58742/Products?name=Keychron
# example 127.0.0.1:58742/Products?in_type=Lips
@app.get("/Products")
async def	products(name:Optional[str] = None, in_type:Optional[str] = None):
	return (product_cat.browse_product(name, in_type))

@app.get("/Products/{product_id}")
async def	view_product(product_id : str):
	return (product_cat.view_product(product_id))

@app.get("/Users/{username}")
async def	view_user_detail(username : str):
	# need to check searching name is a guy who search or not ... but how? -> Ohm said it's FRONTEND problem so yeah im not gonna do it.
	print(shop.users)
	if (shop.get_user_by_username(username)):
		return (shop.get_user_by_username(username).get_user_detail())
	return ("KO")
	# return ("H)

@app.get("/Users/{username}/cart")
async def	view_cart(username : str):
	# need to check searching name is a guy who search or not ... but how? -> im won't do this one neither.
	return (shop.get_user_by_username(username).shopping_cart.show_cart())

@app.get("/Products/{product_id}/add_to_cart")
async def	add_to_cart(username:str, product_id:str, quantity:int):
	ret = shop.get_user_by_username(username).shopping_cart.add_to_cart(product_cat.get_inst_product_by_id(product_id), quantity)
	if (ret):
		return (ret)
	return ("KO")

@app.post("/cart/checkout")
async def	checkout(data:dict):
	user = shop.get_user_by_username(data["username"])
	if (user.make_purchase(user.address[data["address_index"]])):
		return ("OK")
	return ("KO")

@app.post("/Auth/login")
async def	login(data:dict):
	user = User(0)
	if (user.login(data["username"], data["password"])):
		return (data["username"])
	return ("KO")

@app.post("/Auth/register")
async def	register(data:dict):
	guest = Guest()
	new = guest.register(data["username"], data["email"], data["password"]) 
	if (new):
		shop.users.append(new)
		return (new.name)
	return ("KO")

@app.post("/Auth/logout")
async def	logout(data:dict):
	if (shop.get_user_by_username(data["username"]).logout()):
		return ("OK")
	return ("KO")

@app.post("/Users/{username}/orders")
async def	get_orders(username):
	print(shop.get_user_by_username(username).order)
	return (shop.get_user_by_username(username).get_user_order())

@app.get("/Users/{username}/confirm_payment")
async def	confirm_payment(order_id, username, amount:int):
	order = shop.get_user_by_username(username).get_order_by_id(order_id)
	if (not order):
		return ("KO")
	if (order.confirm_payment(amount)):
		return ("OK")
	return ("KO")

@app.get("/feat/orders")
async def	view_order(email, order_id):
	ret = shop.get_user_by_email(email).get_order_by_id(order_id).get_order_detail()
	if (ret):
		return (ret)
	return ("KO")

@app.post("/users/{username}/editinfo")
async def	change_info(username, data:dict):
	user = shop.get_user_by_username(username)
	user.name = data["new_name"]
	user.tel = data["new_tel"]

@app.post("/users/{username}/add_address")
async def	add_address(name, address, tel, username, type:int = 0):
	user = shop.get_user_by_username(username)
	if (type == 0):
		addr = ShippingAddress(name, address, tel)
	elif (type == 1):
		addr = TaxInvoiceAddress(name, address, tel)
	else:
		return ("KO")
	user.address.append(addr)
	return ("OK")

@app.delete("/users/{username}/del_address")
async def	del_address(address_index:int, username):
	user = shop.get_user_by_username(username)
	user.address.pop(address_index)
	return ("OK")

@app.post("/users/{username}/change_password")
async def	change_pass(data:dict):
	user = shop.get_user_by_username(data["username"])
	user.account.password = data["new_pass"]
	return ("OK")

# ADMIN SIDE API 



@app.post("/admin/login")
async def	admin_login(data:dict):
	print(data["username"])
	print(data["password"])
	user = User(0)
	if (user.login(data["username"], data["password"], 1)):
		return (data["username"])
	return ("KO")

@app.post("/admin/register")
async def	add_new_admin(name, salary:int, username, email, password):
	new_admin = Admin(name, salary, username, email, password)
	if (new_admin.register(username, email)):
		return (username)
	return ("KO")

@app.post("/admin/add_product")
async def	add_product(data: dict): #p_type example : "Lips,Eye" (NO SPACE, ONLY COMMA(,))
	product_cat.add_product(data["name"], data["price"], data["specify"], data["stock"], data["description"], data["detail"], data["p_type"])
	return ("OK")

@app.post("/admin/modify_product/{target_product_id}")
async def	modify_product(target_product_id, data:dict):
	if (product_cat.modify_product(target_product_id, data["product_name"], int(data["product_price"]), data["product_description"], data["product_detail"], data["product_type"], int(data["product_stock"]), data["product_specify"])):
		return ("OK")
	return ("KO")

@app.post("/admin/add_promotion")
async def	add_promotion(data:dict):
	if (shop.add_promotion(str(data["product_ids"]), datetime(int(data["year_start"]), int(data["month_start"]), int(data["month_end"])), datetime(int(data["year_end"]), int(data["month_end"]), int(data["day_end"])), int(data["discount"]))):
		return (data["product_ids"])
	return ("KO")

@app.delete("/admin/del_product/{product_id}")
async def	del_product(product_id:str):
	target_product = product_cat.get_inst_product_by_id(product_id)
	if (target_product == None):
		return ("KO")
	product_cat.products.remove(target_product)
	return ("OK")

@app.get("/admin/orders")
async def	browse_orders():
	return (shop.browse_orders())

@app.get("/admin/products")
async def	admin_browse_products(name:Optional[str] = None, in_type:Optional[str] = None):
	return (product_cat.browse_product(name, in_type, all = True))

@app.get("/admin/promotions")
async def	browse_promotions():
	return (shop.promotions)

