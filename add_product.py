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


class ProductCatalog:
	def __init__ (self, first_create):
		self.last_update = first_create
		self.product_list = []
		
	def add_product (self, product):
		self.product_list.append(product)

pc = ProductCatalog("1/1/1")

product_1 = Product("65010030","Jelly Tint", 259, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lib"],9,"#07")
product_2 = Product("65010134","EST. HARDDER 2", 229, "nothing here", "This is another detaikl",["Lib"],1,"#31")

pc.add_product(product_1)

for product in pc.product_list:
	print(product.product_name)




