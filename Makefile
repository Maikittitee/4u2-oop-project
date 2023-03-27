SRCS = add_to_cart.py
CLASS = class.py

all :
	python3 $(CLASS) 

add_to_cart :
	python3 add_to_cart.py

re : all