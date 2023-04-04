from classes import *
from datetime import datetime
from classes import shop
from fastapi import FastAPI


current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
product_cat = ProductCatalog(current_time)
product_cat.add_product("Jelly Tint", 259, "#07", 9, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lips"])
product_cat.add_product("EST. HARDDER 2", 229, "#31", 1, "nothing here", "This is another detaikl", ["Lips"])
product_cat.add_product("Keychorn Q1", 6790, "Blue", 12, "First Keychron custom keyboard","This is magic thing, just but it and type 300wpm",["keyboard","gadget"])
# promo = Promotion([product_1],"1/1/2022","31/12/2023", 39)
# promo2 = Promotion([product_2],"1/1/2022","31/12/2023", 100)
# product_cat.products.append(product_1)
# product_cat.products.append(product_2)
# shop.promotions.append(promo)
# shop.promotions.append(promo2)
# shop.promotions.append(promo2)
cart = ShoppingCart(shop.promotions)
# cart.add_to_cart(product_1,3)
# cart.add_to_cart(product_2,2)
admin_1 = Admin("Nonene",2000,shop)
admin_2 = Admin("Peachji",1,shop)


app = FastAPI()


@app.get("/")
def	root():
	return ({"msg":"Welcome to root path, there are nothing here, better specofic path  , for example , /products or /users"})

@app.get("/Products")
def	products():
	return (product_cat.browse_product(None, None))


@app.get("/Products/name/{name}")
def	products(name):
	return (product_cat.browse_product(name, None))


@app.get("/Products/type/{type_ip}")
def	products(type_ip:str):
	return (product_cat.browse_product(None, type_ip))

print(product_cat.browse_product(None,"Lips"))