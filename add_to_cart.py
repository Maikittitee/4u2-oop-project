
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

class	Item:
	def	__init__(self, product, quantity, promotion):
		self.product = product
		self.quantity = quantity
		self.promotion = promotion

	def show_product_name(self):
		print(self.product.product_name)

class	Promotion:
	def __init__(self, products_id:list, start_date, end_date, discount):
		self.list = products_id
		self.start_date = start_date
		self.end_date = end_date
		self.discount = discount

class	ShoppingCart:
	def __init__(self,promotions):
		self.items = []
		self.promotion = promotions
		
	def get_promotion(self, product):
		for avaiable_product_id in self.promotion.list:
			if (avaiable_product_id == product.product_id):
				return (self.promotion)
		return (None)

	def	add_to_cart(self, product, quantity):
		item = Item(product, quantity, self.get_promotion(product))
		self.items.append(item)
	
	def	show_cart(self):
		i = 1
		total = 0
		for item in self.items:
			if (item.promotion != None):
				print(f"{i}. {item.product.product_name}\t{item.product.product_specify}\tprice: {item.product.product_price} ฿ --> {item.product.product_price * ((100 - self.promotion.discount)/100)} x {item.quantity} : {item.product.product_price * ((100 - self.promotion.discount)/100) * item.quantity}")
				item.product.product_price * ((100 - self.promotion.discount)/100) * item.quantity
			else:
				print(f"{i}. {item.product.product_name}\t{item.product.product_specify}\tprice: {item.product.product_price} ฿ x {item.quantity} : {item.product.product_price * item.quantity}")
				total += item.product.product_price * item.quantity
			i += 1
		print(f"Total amount : {total}฿")
	

product_1 = Product("65010030","Jelly Tint", 259, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lib"],9,"#07")
product_2 = Product("65010134","EST. HARDDER 2", 229, "nothing here", "This is another detaikl",["Lib"],1,"#31")
promo = Promotion(["65010030"],"1/1/2022","31/12/2023", 39)
cart = ShoppingCart(promo)
cart.add_to_cart(product_1,3)
cart.add_to_cart(product_2,2)
cart.show_cart()
#print()
#print(product_1.product_detail)

#print(cart.get_promotion(product_1))
