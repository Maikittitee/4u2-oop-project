from enum import Enum

class Shop:
	def __init__(self):
		self.product_catalog = [] #AGRET ProductCatalog
		self.users = [] #AGGRESION User
		self.promotions = [] # AGGRESTION Promotion
		
class	Order:
	def __init__ (self, order_id):
		self.order_id = order_id
		self.date_crate = None

	def return_order_detail(self):

		view_order_detail = {
			"order_id" : self.order_id,
			"date_crate" : self.date_crate
		}
		return (view_order_detail)
		

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
		
class	ShippingStatus(Enum):
	NONSHIP = 0
	IN_SHIPPING = 1
	DELIVERED = 2

class	OrderStatus(Enum):
	CANCELED = 0
	PENDING = 1
	CONFRIMED = 2

order_01 = Order("orderrrr")
order_01.order_id = "000001"
order_01.date_crate = "03/04/2023"

print(order_01.return_order_detail())