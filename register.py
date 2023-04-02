class Shop:
	def __init__(self):
		self.product_catalog = [] #AGRET ProductCatalog
		self.users = [] #AGGRESION User
		self.promotions = [] # AGGRESTION Promotion


class User:
	def __init__ (self, user_id, email, name, password):
		self.user_id = user_id
		self.email = email
		self.name = name
		self.account = Account(email, password)

class UserCatalog():
    def __init__(self):
        self.users = []

    def save_users(self,user_list):
        self.users = user_list
	
		
class Account:
	def __init__ (self, email, password):
		self.email = email
		self.password = password

class Admin(User):
	def __init__ (self, salary):
		self.salary = salary


new_user1 = User("id","admin@gmail.com", "Nita", "12345")
new_user2 = User("id","admin2@gmail.com", "IPY", "12345")

user_catalog = UserCatalog()
user_catalog.save_users([new_user1, new_user2])

for user in user_catalog.users:
	print(user.name)
