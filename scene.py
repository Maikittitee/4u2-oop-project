from classes_with_method import *
from datetime import datetime
import json


product_cat.add_product("Jelly Tint", 259, "#07", 9, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lips"])
product_cat.add_product("EST. HARDDER 2", 229, "#31", 1, "nothing here", "This is another detaikl", ["Lips"])
product_cat.add_product("Keychorn Q1", 6790, "Blue", 12, "First Keychron custom keyboard","This is magic thing, just buy it and typing 300wpm",["keyboard","gadget"])


admin = Admin("I'm Admin",10000,shop,"admin1","admin@gmail.com","pass")
guest = Guest()
customer = guest.register("user","m@gmail.com","pass")
if (customer.login("user","pass")):
	print("login Sucess")

shop.add_promotion(["1","2"], datetime(2004,4,9), datetime(2025,4,9), 50)
customer.shopping_cart.add_to_cart(product_cat.get_inst_product_by_id("1"), 2)
customer.shopping_cart.add_to_cart(product_cat.get_inst_product_by_id("2"), 1)
print(f"{Colors.HEADER}#############\n# SHOW CART #\n#############{Colors.ENDC}")
print(json.dumps(customer.shopping_cart.show_cart(), indent = 4))
customer.make_purchase()

print(f"{Colors.HEADER}#############\n#   ORDER   #\n#############{Colors.ENDC}")
print(json.dumps(customer.get_user_order(), indent = 4))

print(customer.get_order_by_id("1").make_payment(100000000))

print(f"{Colors.HEADER}#############\n#   ORDER NEWWWW  #\n#############{Colors.ENDC}")
print(json.dumps(customer.get_user_order(), indent = 4))

# print(product_cat.get_inst_product_by_id("1"));
# print(product_cat.get_inst_product_by_id("2"));




# for promotion in shop.promotions:
#     print(promotion.products)

    
# print("HELLO")