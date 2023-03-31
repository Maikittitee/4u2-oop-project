# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 23:17:03 by ktunchar          #+#    #+#              #
#    Updated: 2023/04/01 02:24:20 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a implement of every class that came from class diagram
# TODO : Relation

from datetime import datetime
import time
from enum import Enum
from typing import Optional
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
		self.products = []

	def	product_id_genarator(self,name:str):
		return (f"{name}Assumethisisproductid")

	def	add_product(self, name, price, specify, stock, description, detail, p_type):
		new_product = Product(self.product_id_genarator(name),name,price, description, detail, p_type, stock, specify)
		self.products.append(new_product)
		self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 


	def	browse_product (self, name : Optional[str] = None, type_input : Optional[str] = None) -> None:
		product_list = []
		if (type_input != None):
			for product in self.products:
				if (type_input in product.type):
					product_list.append(product)
		elif (name != None):
			for product in self.products:
				if (name in product.name):
					product_list.append(product)
		else:
			product_list = self.products
		ret_dict = {}
		count_product = 0
		for product in product_list:
			count_product += 1
			ret_dict[product.name] = product.get_product_detail()
		ret_dict["__count_product"]:count_product
		return (ret_dict)


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

	def	get_product_detail(self):
		return ({
		"id" : self.id, 
		"name" : self.name,
		"price" : self.price, 
		"description" : self.description, 
		"detail" : self.detail, 
		"type" : self.type,
		"stock" : self.stock,
		"specify" : self.specify
		})

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

class	UserStatus(Enum):
	ONLINE = 1
	OFFLINE = 0
class User:
	def __init__ (self, user_id, email, name):
		self.user_id = user_id
		self.email = email
		self.name = name
		self.status = UserStatus.OFFLINE
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
					return (promotion)
		return (None)

	def	add_to_cart(self, product, quantity):
		item = Item(product, quantity, self.get_promotion(product))
		self.items.append(item)
	
	def	show_cart(self):
		total = 0
		ret_dict = {}
		ret_dict["__cart_id"] = self.cart_id
		for item in self.items:
			if (item.promotion != None):
				total += (item.product.price * (100 - item.promotion.discount)/100 * item.quantity)
				ret_dict[item.product.name] = {
					"product_price":item.product.price,
					"discount":item.promotion.discount,
					"price_after_discount": item.product.price * (100 - item.promotion.discount)/100 ,
					"quantity":item.quantity,
					"price":item.quantity * item.product.price * (100 - item.promotion.discount)/100 
				}
			else:
				total += (item.product.price * item.quantity)
				ret_dict[item.product.name] = {
					"product_price":item.product.price,
					"discount":0,
					"price_after_discount": item.product.price  ,
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

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
product_cat = ProductCatalog(current_time)
product_1 = Product("65010030","Jelly Tint", 259, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lips"],9,"#07")
product_2 = Product("65010134","EST. HARDDER 2", 229, "nothing here", "This is another detaikl",["d"],1,"#31")
product_cat.add_product("newwww",123,"green",12,"haha","ha",["key"])
promo = Promotion([product_1],"1/1/2022","31/12/2023", 39)
promo2 = Promotion([product_2],"1/1/2022","31/12/2023", 100)
product_cat.products.append(product_1)
product_cat.products.append(product_2)
shop.promotions.append(promo)
shop.promotions.append(promo2)
# shop.promotions.append(promo2)
# cart = ShoppingCart("This is a Cart ID",shop.promotions)
# cart.add_to_cart(product_1,3)
# cart.add_to_cart(product_2,2)

# print(json.dumps(cart.show_cart(),indent = 4))
# print(cart.promotions)

print(json.dumps(product_cat.browse_product(),indent = 4))
# print(product_cat.last_update)

