all:
	python3 main.py
api:
	python3 -m uvicorn main:app --reload && \
	open http://127.0.0.1:8000
