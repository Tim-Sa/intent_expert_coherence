test:
	pytest tests/api_test.py

t:
	make test

basic_startup:
	uvicorn src.api.main:app --reload

bs:
	make basic_startup