.DEFAULT_GOAL := help
.PHONY: setup dbt-docs remake run-web help

GREEN = $(shell echo "\033[32m")
YELLOW = $(shell echo "\033[33m")
RESET = $(shell echo "\033[0m")

VENV_NAME?=.venv
PYTHON=$(VENV_NAME)/bin/python

setup: ## Activate the virtual environment, creating it if needed
	@if [ -d "$(VENV_NAME)" ]; then \
		echo "$(YELLOW)$(VENV_NAME) already exists. Skipping package installation.$(RESET)"; \
	else \
		echo "$(GREEN)Creating virtual environment and installing packages...$(RESET)"; \
		python3 -m venv $(VENV_NAME); \
		$(PYTHON) -m pip install -U pip; \
		$(PYTHON) -m pip install -Ur requirements.txt; \
	fi
	@echo "$(GREEN)Virtual environment setup complete.$(RESET)"


run-web: ## Run the Flask application locally
	@if [ -d "$(VENV_NAME)" ]; then \
		$(PYTHON) script.py; \
	else \
		echo "$(YELLOW)Virtual environment not created. Run 'make setup' first.$(RESET)"; \
	fi

remake: ## Delete the virtual environment
	@rm -rf $(VENV_NAME)
	@echo "$(GREEN)Virtual environment removed.$(RESET)"

help: ## Show targets and comments (must have ##)
	@grep -h "##" $(MAKEFILE_LIST) | grep -v grep | sed -e 's/\\$$//' | sed -e 's/##//'
