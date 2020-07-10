SERVICE_NAME := $(notdir $(CURDIR))
# HELP
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS
build: ## Build the container
	docker build -t $(SERVICE_NAME) .

build-nc: ## Build the container without caching
	docker build --no-cache -t $(SERVICE_NAME) .

run-local: ## Run container on port configured in `config.env`
	cd api/
	python -m flask run -p 5001

run: ## Run container on port configured in `config.env`
	docker run -p=5001:5000 --name=$(SERVICE_NAME) $(SERVICE_NAME)

up: build run ## Run container on port configured in `config.env` (Alias to run)

attach: ## Attach a bash session to the container
	docker exec -it $(SERVICE_NAME) bash

logs: ## tail logs for the container
	docker logs -f $(SERVICE_NAME)

stop: ## Stop and remove a running container
	docker stop $(SERVICE_NAME); docker rm $(SERVICE_NAME)

clean: ## Remove container image
	docker rmi -f $(SERVICE_NAME)