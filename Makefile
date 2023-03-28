
all:
	python3 main.py
api:
	python3 -m uvicorn browse_product:app --reload