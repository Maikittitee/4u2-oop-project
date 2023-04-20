# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes_with_method.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 23:17:03 by ktunchar          #+#    #+#              #
#    Updated: 2023/04/20 23:40:35 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a implement of every class that came from class diagram

from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import Optional


#current_date = datetime(datetime.year, datetime.month, datetime.day)

class ID:
    def __init__(self):
        self.__id_count = 0

    def generateID(self):
        self.__id_count += 1
        return str(self.__id_count)

admin_id_gen = ID()
user_id_gen = ID()
cart_id_gen = ID()
product_id_gen = ID()
payment_id_gen = ID()
order_id_gen = ID()
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
class ProductCatalog:
	def __init__ (self, first_create):
		self.products = []


	def	add_product(self, name, price, specify, stock, description, detail, p_type):
		self.products.append(Product(name,price, description, detail, p_type, stock, specify))
	
	def	delete_product(self, product_id):
		product = self.get_inst_product_by_id(product_id)
		self.products.remove(product)  

	def get_product_detail_by_id(self, id):
		for product in self.products:
			if (product.id == id):
				return (product.get_product_detail())
			
	def get_inst_product_by_id(self, id):
		for product in self.products:
			if (product.id == id):
				return (product)
			
	def get_products_by_id(self, id):
		products = []
		target_product_name = self.get_inst_product_by_id(id).name
		for product in self.products:
			if (product.name == target_product_name):
				products.append(product)
		return (products)

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
		return(self.remove_dup_product(product_list))
	
	def	remove_dup_product(self, products):
		new_products = []
		for product in products:
			if (not product.already_exist_in(new_products)):
				new_products.append(product)
		return (new_products)


	
	def view_product(self, product_id):
		# this method need to implement all the same product but difference SPECIFY and each left stock
		products = self.get_products_by_id(product_id)
		specify_dict = {}
		for product in products:
			specify_dict.update({product.specify: product.stock})
			p2 = product
		p1 = products[0]
		ret_dict = {
		"id" : 		f"{p1.id}-{p2.id}", 
		"name" :	p1.name,
		"price" : 	p1.price, 
		"description" : p1.description, 
		"detail" : p1.detail, 
		"type" : p1.type,
		"specify" : specify_dict
		}
		return (ret_dict)
		
	def	modify_product(self, target_product_id,product_name=None, product_price=None, product_description=None, product_detail=None, product_type=None, product_stock=None, product_specify=None):
		product = self.get_inst_product_by_id(target_product_id)
		if (product_price != None and product_stock != None and (product_price < 0 or product_stock < 0)):
			return (0)
		if (product_name != None):
			product.name = product_name
		if (product_price != None):
			product.price = product_price
		if (product_description != None):
			product.description = product_description
		if (product_detail != None):
			product.detail = product_detail
		if (product_type != None):
			product.type = product_type
		if (product_stock != None):
			product.stock = product_stock
		if (product_specify != None):
			product.specify = product_specify
		return (product)

product_cat = ProductCatalog("aaa")

class Shop:
	def __init__(self):
		self.product_catalog = product_cat #AGRET ProductCatalog
		self.users = [] #AGGRESION User --> # KEEP ONLY AUTHENTICATIONUSER !!!
		self.promotions = [] # AGGRESTION Promotion\

	def	add_promotion(self, product_ids, date_start, date_end, discount):
		products = []
		for product_id in product_ids:
			products.append(self.product_catalog.get_inst_product_by_id(product_id))
		self.promotions.append(Promotion(products, date_start, date_end, discount))

	def	browse_order(self):
		ret_dict = {}
		for user in self.users:
			for order in user.orders:
				ret_dict.update({user.name : order.get_order_detail()})

	def get_user_by_username(self, username):
		for user in self.users:
			if (user.name == username):
				return (user)
		return (None)
	
shop = Shop()

#########################################################
# ---------------------- PRODUCT ---------------------- #
#########################################################

class	Product:
	def __init__(self, product_name:str, product_price:int, product_description: str, product_detail : str, product_type : list, product_stock : int, product_specify : str):
		self.id =  product_id_gen.generateID()
		self.__name = product_name
		self.price = product_price
		self.description = product_description
		self.detail = product_detail
		self.type = product_type
		self.stock = product_stock
		self.specify = product_specify

	@property 
	def	name(self):
		return(self.__name)
	
	def already_exist_in(self, product_list):
		for product in product_list:
			if (self.is_same_name(product)):
				return (1)
		return (0)


	def	is_same_name(self, product):
		return (self.name == product.name)
	

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

	def	is_available(self):
		if (self.quantity <= self.product.stock):
			return (1)
		return (0)
	
	def get_item_detail(self):
		ret_dict = {}
		# if (self.promotion != None):
		ret_dict[self.product.id] = {
			"product_name":self.product.name,
			"product_price":self.product.price,
			"discount":self.promotion.discount,
			"price_after_discount": self.product.price * (100 - self.promotion.discount)/100 ,
			"quantity":self.quantity,
			"price":self.quantity * self.product.price * (100 - self.promotion.discount)/100 
		}
		return (ret_dict)

class	Promotion:
	def	__init__ (self, product_list:list,date_start, date_end, discount):
		self.date_start = date_start
		self.date_end = date_end
		self.discount = discount
		self.products = product_list # COMPOSITION Product

	def is_promotion_available(self):
		today = datetime.now()
		if (self.date_end == None or self.date_start == None):
			return (1)
		if (self.date_start <= today <= self.date_end):
			return (1)
		return (0)

#########################################################
# ----------------------- USER ------------------------ #
#########################################################
class Account:
	def __init__ (self, email, password):
		self.email = email
		self.password = password

class	UserStatus(Enum):
	ONLINE = 1
	OFFLINE = 0

class User: #ABTRACT CLASS ...... STOPPPP DONT ASK ME ANYTHING > EVERY CLASS CAN BE ABTRACT CLASS
	def	__init__(self,id):
		self.user_id = id
		self.name = None
		self.shop = shop
		self.status = UserStatus.OFFLINE

	def	login(self,username, password):
		for user in self.shop.users:
			if (username == user.name):
				if (password == user.account.password):
					user.status = UserStatus.ONLINE
					return (1)
				else:
					return (0)
		return (0)

	def	logout(self):
		self.status = UserStatus.OFFLINE

class Admin(User):
	count = 0
	def __init__ (self, name,salary, shop, username, email, password):
		User.__init__(self,f"admin{admin_id_gen.generateID()}")
		self.account = Account(email, password) 
		self.salary = salary
		self.name = username

class Customer(User):
	def __init__ (self):
		User.__init__(self,user_id_gen.generateID())
		self.shopping_cart = ShoppingCart() # Association ShoppingCart 

	

class Guest(Customer):
	def	__init__ (self):
		Customer.__init__(self)

	def	register(self, username, email, password):

		for customer in self.shop.users:
			if (username == customer.name):
				return (0)
		for user in self.shop.users:
			if (email == user.account.email):
				return (0)
			
		new_customer = AuthenticationUser(username, email, password)
		
		self.shop.users.append(new_customer)
		return (new_customer)

class AuthenticationUser(Customer):
	def	__init__ (self, username, email, password):
		Customer.__init__(self)
		self.name = username
		self.address = None
		self.account = Account(email, password)
		self.order = [] # Aggretion Order
		self.favorite = []

	def	get_order_by_id(self, order_id):
		for order in self.order:
			if (order.order_id == order_id):
				return (order)
		return (None)

	def set_address(self, new_addr):
		self.address = new_addr

	def	get_user_detail(self):
		return (
		{
			"user_id" : self.user_id,
			"user_name": self.name,
			"user_status": f"{self.status}",
			"user_account":{
				"email":self.account.email,
				"password":self.account.password
			},
			"user_shopping_cart":self.shopping_cart.show_cart(),
			"user_order":self.get_user_order(),
			"user_favorite":self.get_user_favorite()
		}
		)
	def	get_user_order(self):
		ret_dict = {}
		for order in self.order:
			ret_dict.update({order.order_id : order.get_order_detail()})
		return (ret_dict)

	def	get_user_favorite(self):
		return ("Yang Mai dai Tum")
		
	def make_purchase(self):
		new_order = self.shopping_cart.checkout(self)
		if (new_order): 
			self.order.append(new_order)
			self.shopping_cart.clear()
			return (1)
		return (0)
	
	def	make_payment(self, order_id, evi):
		order = self.get_order_by_id(order_id)



#########################################################
# --------------------- User Hold --------------------- #
#########################################################

class	ShoppingCart:
	def __init__ (self):
		self.promotions = shop.promotions # Association Promotion (but it accully need to keep ALL Promotion then it's better if we use Shop)
		self.items = [] # Aggretion Item

	def get_promotion(self, product):
		for promotion in self.promotions:
			for avaiable_product in promotion.products :
				if (avaiable_product is product and promotion.is_promotion_available()):
					return (promotion)
		return (Promotion([product], None, None, 0))

	def clear(self):
		self.items = []

	def	add_to_cart(self, product, quantity):
		if (product.stock < quantity):
			return (0)
		item = Item(product, quantity, self.get_promotion(product)) 
		self.items.append(item)
		return (item.get_item_detail())
	
	def get_item_by_index(self, index):
		count = 0
		for item in self.items:
			if (index == count):
				return (item)
			count += 1
		return (0)
	
	def remove_from_cart(self, index_of_item):
		self.change_quantity(self.get_item_by_index(index_of_item).quantity, index_of_item)

	def	change_quantity(self, num ,index_of_item):
		count = 0
		selected_item = self.get_item_by_index(index_of_item)
		selected_item.quantity += num
		if (selected_item.quantity == 0):
			self.items.remove(selected_item)

	def	check_promotion(self):
		for item in self.items:
			if (item.promotion != None and not item.promotion.is_promotion_available()):
				item.promotion = None
			
	def	show_cart(self):
		total = 0
		ret_dict = {
			"available_item": {},
			"unavailable_item": {}	
		}
		self.check_promotion()
		for item in self.items:
			if (item.is_available()):
				ret_dict["available_item"].update(item.get_item_detail())
			else:
				ret_dict["unavailable_item"].update(item.get_item_detail())

		ret_dict["total"] = self.cal_total()
		return (ret_dict)
	
	def	cal_total(self):
		total = 0
		self.check_promotion()
		for item in self.items:
			if (item.is_available()):
				total += item.product.price * (100 - item.promotion.discount)/100 * item.quantity
		return (total)

	def	checkout(self,user):
		new_item_list = []
		self.check_promotion()
		for item in self.items:
			if (item.is_available()):
				new_item_list.append(item)

		if (len(new_item_list) != 0):	
			new = Order(order_id_gen.generateID(), datetime.now(), user)
			for item in new_item_list:
				item.product.stock -= item.quantity
			new.items = new_item_list
			return new
		else:
			return (0)

class	Order:
	def __init__ (self, order_id, date_create, user):
		self.user = user
		self.order_id = order_id
		self.date_create = str(date_create)
		self.items = [] # Agrettion Items
		self.shipping_info = None # Agrettion ShippingInfo
		self.payment = Payment(payment_id_gen.generateID(), 0, OrderStatus.PENDING, self) # Asso Payment
	
	def get_order_detail(self):
		item_dict = {}
		for item in self.items:
			item_dict.update({item.product.id:item.get_item_detail()})
		return {
			"user":self.user.name,
			"id":self.order_id,
			"payment_status":str(self.payment.status),
			"create":self.date_create,
			"items":item_dict,
			"total":self.cal_total()
		}
	
	def	cal_total(self):
		total = 0
		for item in self.items:
			total += item.product.price * (100 - item.promotion.discount)/100 * item.quantity
		return (total)

	def	make_payment(self, amount):
		if (amount >= self.cal_total()):
			self.payment.status = OrderStatus.CONFIRMED
			self.shipping_info = ShippingInfo(self.user.address, ShippingStatus.NONSHIP, None, None)
			return (1)
		return (0)

	def	edit_shipping_info(self, address = None,  date_shipping = None, date_delivered = None):
		if (address != None):
			self.shipping_info.address = address
		if (date_shipping != None):
			self.date_shipping = date_shipping
		if (date_delivered != None):
			self.date_delivered = date_delivered
		
class	Payment:
	def	__init__ (self, payment_id, amount, status, order):
		self.order = order
		self.payment_id = payment_id
		self.amount = amount
		self.status = status
		self.evidence = None

class	ShippingInfo:
	def	__init__ (self, address,shipping_status, date_shipping, date_delivered):
		self.shipping_status = shipping_status
		self.address = address
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
	CONFIRMED = 2

