from datetime import datetime
from fastapi import FastAPI
from typing import Optional
from enum import Enum



app = FastAPI()

class	SearchBy(Enum):
	NAME = 1,
	TYPE = 2

class ProductCatalog:
	def __init__ (self, first_create):
		self.last_update = first_create
		self.product_list = []

	def	browse_product(self, search_type:Optional[int] = None, input : Optional[str] = None) -> None:
		product_list = []
		#print(f"sarch_type is {input} and input is ")
		if (search_type == 1):
			for product_obj in self.product_list:
				if (input in product_obj.name):
					product_list.append(product_obj)
		elif (search_type == 2):
			for product_obj in self.product_list:
				for product_type in product_obj.type:
					if (product_type == input):
						product_list.append(product_obj)
		else:
			# print("what the fuck")
			product_list = self.product_list

		product_dict = {}
		for product in product_list:
			product_dict[product.name] = product.get_product_detail()
		return (product_dict)


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

	def __str__(self):
		return (self.name)

	def	get_product_detail(self):
		ret_dict = {
			"id": self.id,
			"name": self.name,
			"price": self.price,
			"description":self.description,
			"detail":self.detail,
			"type":self.type,
			"stock":self.stock,
			"specify":self.specify
		}
		return (ret_dict)


# Setup Scenario
product_catalog = ProductCatalog(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
p1 = Product("65010030","Magic Lips",350,"(null)","(null)",["Lips"],12,"pink")
p2 = Product("65010134","Keychorn Q1",6790,"(null)","(null)",["Keyboard"],1,"blue")
product_catalog.product_list.append(p1)
product_catalog.product_list.append(p2)
#print(product_catalog.browse_product())



# API 

@app.get("/Products")
def	get_name():
	return product_catalog.browse_product()

@app.get("/Products/Name/{input}")
def	get_name(input):
	return product_catalog.browse_product(1, input)

@app.get("/Products/Type/{input}")
def	get_name(input):
	return product_catalog.browse_product(2, input)
#################################
# 				debug			#
#################################
# product_catalog.browse_product(SearchBy.TYPE, ["Keyboard"])
# print(product_catalog.browse_product(1, "Key"))

# print(SearchBy.NAME)
