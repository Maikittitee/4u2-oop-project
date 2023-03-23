# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 23:17:03 by ktunchar          #+#    #+#              #
#    Updated: 2023/03/23 19:46:31 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a implement of every class that came from class diagram
# TODO : Relation

from datetime import datetime
import time
from enum import Enum


################################################################
# --------------------- MANAGEMENT CLASS --------------------- #
################################################################

class Shop:
	def __init__(self):
		pass

class ProductCatalog:
	def __init__ (self, first_create):
		self.last_update = first_create
		self.product_list = []


#########################################################
# ---------------------- PRODUCT ---------------------- #
#########################################################


class	Product:
	def __init__(self, product_id : str, product_name:str, product_price:int, product_description: str, product_detail : str, product_type : list, product_stock : int, product_specify : str):
		self.product_id =  product_id
		self.product_name = product_name
		self.product_price = product_price
		self.product_description = product_description
		self.product_detail = product_detail
		self.product_type = product_type
		self.product_stock = product_stock
		self.product_specify = product_specify

class	Promotion:
	def	__init__ (self, date_start, date_end, discount):
		self.date_start = date_start
		self.date_end = date_end
		self.discount = discount

class	Item:
	def	__init__ (self, quanity):
		self.quanity = quanity



#########################################################
# ----------------------- USER ------------------------ #
#########################################################

class User:
	def __init__ (self, user_id, email, name):
		self.user_id = user_id
		self.email = email
		self.name = name

class Account:
	def __init__ (self, email):
		self.email = email

class Admin(User):
	def __init__ (self, salary):
		self.salary = salary

class Customer(User):
	def __init__ (self):
		pass

class Guest(Customer):
	def	__init__ (self):
		pass

class AuthenticationUser(Customer):
	def	__init__ (self, address):
		self.address = address
		self.order = []

#########################################################
# --------------------- User Hold --------------------- #
#########################################################

class	ShoppingCart:
	def __init__ (self, cart_id, total_amount):
		self.cart_id = cart_id
		self.total_amount = total_amount

class	Favorite:
	def	__init__ (self):
		pass

class	Order:
	def __init__ (self, order_id, date_crate):
		self.order_id = order_id
		self.date_crate = date_crate

class	Payment:
	def	__init__ (self, payment_id, amount, status):
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

product = ProductCatalog(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print(product.last_update)
time.sleep(10)
print(product.last_update)

