all:
	python3 main.py
api:
	open http://127.0.0.1:8000 ; \
	python3 -m uvicorn main:app --reload
