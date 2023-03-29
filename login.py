

# print(email_input)
# print(password_input)


class Shop:
	def __init__(self):
		self.product_catalog = [] #AGRET ProductCatalog
		self.users = [] #AGGRESION User
		self.promotions = [] # AGGRESTION Promotion
		
shop = Shop()

class User():
    def __init__ (self, user_id, email, name, shop):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.account = None
        self.shop_k = shop
	
    def	login(self, email_input, password_input):
        for user in self.shop_k.users:
            if (email_input == user.account.email) and (password_input == user.account.password):
                print("Login Successfully")
                return 1
        print("Invalid Authntication")

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
		pass
        # self.shopping_cart = ShoppingCart('SC' + user_id) # Association ShoppingCart 
	
class Guest(Customer):
	def	__init__ (self):
		pass

class AuthenticationUser(Customer):
	def	__init__ (self, address):
		self.address = address
		self.order = [] # Aggretion Order
		# self.favorite = Favorite() #  Association Favorite
                

Atheuser1 = User("id","email@gmail.com","nita",shop)
account1 = Account("haha@gmail.com","pass")
Atheuser1.account = account1
shop.users.append(Atheuser1)

new_user_login = User(None,None,None,None)
new_user_login.shop_k = shop


new_user_login.login("haha@gmail.com","pass")



