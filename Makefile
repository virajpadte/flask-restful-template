SERVICE_NAME := $(notdir $(CURDIR))
UNAME := $(shell uname -m)
# HELP
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

run-local-hot-reload: ## Run flask server locally with hot reload to help with fast developement
	cd service; python3 -m flask --debug run -p 5001

deploy-local: ## Run locally using gunicorn server binded on port 8080
#cd service; gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:8080 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --access-logfile .log/access.log --error-logfile .log/error.log
	cd service; gunicorn wsgi:app

#gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info

test-local: ## run pytests locally on the Flask API
	rm -rf .pytest_cache .coverage .pytest_cache service/unit_test_reports && echo "\nRemoved old test generated reports"|| echo "\nDid not find any old test reports"
	cd service && pytest