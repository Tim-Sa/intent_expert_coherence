# direct mode
test:
	pytest tests/test_api.py

t:
	make test

basic_startup:
	uvicorn src.api.main:app --reload

bs:
	make basic_startup


# docker mode
COMPOSE_FILE=docker-compose.yml 
CONTAINER_NAME=intent-api

start:
	docker-compose -f $(COMPOSE_FILE) up -d

stop:
	docker-compose -f $(COMPOSE_FILE) stop

rm:
	docker-compose -f $(COMPOSE_FILE) down

start-interactive:
	docker-compose -f $(COMPOSE_FILE) run --rm $(CONTAINER_NAME)

logs:
	docker-compose -f $(COMPOSE_FILE) logs $(CONTAINER_NAME)

restart: stop start

clean: stop rm

