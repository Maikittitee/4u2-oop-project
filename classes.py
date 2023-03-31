# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 23:17:03 by ktunchar          #+#    #+#              #
#    Updated: 2023/03/31 19:22:08 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a implement of every class that came from class diagram
# TODO : Relation

from datetime import datetime
import time
from enum import Enum
import	json


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

################################################################
# --------------------- MANAGEMENT CLASS --------------------- #
################################################################

class Shop:
	def __init__(self):
		self.product_catalog = [] #AGRET ProductCatalog
		self.users = [] #AGGRESION User
		self.promotions = [] # AGGRESTION Promotion

shop = Shop()

class ProductCatalog:
	def __init__ (self, first_create):
		self.last_update = first_create
		self.product_list = []


#########################################################
# ---------------------- PRODUCT ---------------------- #
#########################################################

class	Product:
	def __init__(self, product_id : str, product_name:str, product_price:int, product_description: str, product_detail : str, product_type : list, product_stock : int, product_specify : str):
		self.id =  product_id
		self.name = product_name
		self.price = product_price
		self.description = product_description
		self.detail = product_detail
		self.type = product_type
		self.stock = product_stock
		self.specify = product_specify

class	Item:
	def	__init__ (self, product, quantity, promotion):
		self.product = product
		self.quantity = quantity
		self.promotion = promotion # Composition Promotion

class	Promotion:
	def	__init__ (self, product_list:list,date_start, date_end, discount):
		self.date_start = date_start
		self.date_end = date_end
		self.discount = discount
		self.products = product_list # COMPOSITION Product





#########################################################
# ----------------------- USER ------------------------ #
#########################################################

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
		self.shopping_cart = ShoppingCart('SC' + self.id) # Association ShoppingCart 

class Guest(Customer):
	def	__init__ (self):
		pass

class AuthenticationUser(Customer):
	def	__init__ (self, address):
		self.address = address
		self.order = [] # Aggretion Order
		self.favorite = Favorite() #  Association Favorite

#########################################################
# --------------------- User Hold --------------------- #
#########################################################

class	ShoppingCart:
	def __init__ (self, cart_id, promotions):
		self.cart_id = cart_id
		self.total_amount = 0
		self.promotions = promotions # Association Promotion (but it accully need to keep ALL Promotion then it's better if we use Shop)
		self.items = [] # Aggretion Item

	def get_promotion(self, product):
		for promotion in self.promotions:
			for avaiable_product in promotion.products :
				if (avaiable_product is product):
					return (self.promotion)
		return (None)

	def	add_to_cart(self, product, quantity):
		item = Item(product, quantity, self.get_promotion(product))
		self.items.append(item)
	
	def	show_cart(self):
		total = 0
		ret_dict = {}
		ret_dict["__cart_id"]=self.cart_id
		for item in self.items:
			total += item.product.price
			ret_dict[item.product.name] = {
				"product_price":item.product.price,
				"quantity":item.quantity,
				"price":item.quantity * item.product.price
			}
		ret_dict["__total"] = total
		return (ret_dict)



class	Favorite:
	def	__init__ (self):
		self.products = [] # Aggretion Product



class	Order:
	def __init__ (self, order_id, date_crate, user):
		self.user = user
		self.order_id = order_id
		self.date_crate = date_crate
		self.items = [] # Agrettion Items
		self.ShippingInfo = [] # Agrettion ShippingInfo
		self.payment = None # Asso Payment
	
	def	cal_total(self):
		pass


class	Payment:
	def	__init__ (self, payment_id, amount, status, order):
		self.order = order
		self.payment_id = payment_id
		self.amount = amount
		self.status = status

class	ShippingInfo:
	def	__init__ (self, shipping_id, shipping_status, tracking_number, date_shipping, date_delivered):
		self.shipping_id = shipping_id
		self.shipping_status = shipping_status
		self.tracking_number = tracking_number
		self.date_shipping = date_shipping
		self.date_delivered = date_delivered

# ENUM #

class	ShippingStatus(Enum):
	NONSHIP = 0
	IN_SHIPPING = 1
	DELIVERED = 2

class	OrderStatus(Enum):
	CANCELED = 0
	PENDING = 1
	CONFRIMED = 2

# product = ProductCatalog(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
# print(product.last_update)
# time.sleep(10)
# print(product.last_update)

product_1 = Product("65010030","Jelly Tint", 259, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lib"],9,"#07")
product_2 = Product("65010134","EST. HARDDER 2", 229, "nothing here", "This is another detaikl",["Lib"],1,"#31")
promo = Promotion(["65010030"],"1/1/2022","31/12/2023", 39)
shop.promotions.append(promo)
cart = ShoppingCart("This is a Cart ID",shop.promotions)
cart.add_to_cart(product_1,3)
cart.add_to_cart(product_2,2)

print(json.dumps(cart.show_cart(),indent = 4))
# for item in cart.items:
# 	print(item.product.name)