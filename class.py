# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    class.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 23:17:03 by ktunchar          #+#    #+#              #
#    Updated: 2023/03/22 01:23:15 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a prototype of every class that came from class diagram

from datetime import datetime
import time

class Shop:
	def __init__(self):
		pass

class ProductCatalog:
	def __init__ (self, first_create):
		self.last_update = first_create
		self.product_list = []


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


product = ProductCatalog(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print(product.last_update)
time.sleep(10)
print(product.last_update)

