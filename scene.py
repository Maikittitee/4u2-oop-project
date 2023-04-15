from classes import *

# product_cat = ProductCatalog("aaaa")

product_cat.add_product("Jelly Tint", 259, "#07", 9, "Magic Lib Tint", "This is detail\nThis lib made by angle that came from heaven\nHave been sell For 10 year",["Lips"])
product_cat.add_product("EST. HARDDER 2", 229, "#31", 1, "nothing here", "This is another detaikl", ["Lips"])
product_cat.add_product("Keychorn Q1", 6790, "Blue", 12, "First Keychron custom keyboard","This is magic thing, just but it and type 300wpm",["keyboard","gadget"])


# #promo = Promotion([product_1],"1/1/2022","31/12/2023", 39)
# # promo2 = Promotion([product_2],"1/1/2022","31/12/2023", 100)
# # shop.promotions.append(promo)
# # shop.promotions.append(promo2)
# cart = ShoppingCart(shop.promotions)
# cart.add_to_cart(product_cat.get_inst_product_by_id("1"),1)
# cart.add_to_cart(product_cat.get_inst_product_by_id("3"),12)
# print(cart.show_cart())

print(product_cat.get_inst_product_by_id("1"));
print(product_cat.get_inst_product_by_id("2"));



shop.add_promotion(["1","2"], "something", "something", 23)

for promotion in shop.promotions:
    print(promotion.products)
    
# print("HELLO")