# direct mode
test:
	pytest tests/

t:
	make test

basic_startup:
	uvicorn src.api.main:app --reload

bs:
	make basic_startup


# docker mode
COMPOSE_FILE=docker-compose.yml 
LOCAL_COMPOSE_FILE=local.docker-compose.yml
CONTAINER_NAME=intent-api
IMAGE_NAME=intent_expert_coherence_intent-api

start:
	docker-compose -f $(COMPOSE_FILE) up -d --build

stop:
	docker-compose -f $(COMPOSE_FILE) stop

rm:
	docker-compose -f $(COMPOSE_FILE) down

start-interactive:
	docker-compose -f $(COMPOSE_FILE) run --rm $(CONTAINER_NAME)

logs:
	docker-compose -f $(COMPOSE_FILE) logs $(CONTAINER_NAME)

restart: stop start

rmi:
	docker rmi -f $(IMAGE_NAME)

clean: stop rm rmi

lstart:
	docker-compose --env-file .local.env -f $(LOCAL_COMPOSE_FILE) up -d --build

lstop:
	docker-compose --env-file .local.env -f $(LOCAL_COMPOSE_FILE) stop

lrm:
	docker-compose --env-file .local.env -f $(LOCAL_COMPOSE_FILE) down

lstart-interactive:
	docker-compose --env-file .local.env -f $(LOCAL_COMPOSE_FILE) run --rm $(CONTAINER_NAME)

llogs:
	docker-compose --env-file .local.env -f $(LOCAL_COMPOSE_FILE) logs $(CONTAINER_NAME)

lrestart: lstop lstart

lclean: lstop lrm rmi

