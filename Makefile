# Windows Makefile
.DEFAULT_GOAL := help
.PHONY: setup

# Color codes for Windows (these will work in some terminals like Windows Terminal, but may not display correctly in Command Prompt)
GREEN = $(shell echo -e "\033[32m")
YELLOW = $(shell echo -e "\033[33m")
RESET = $(shell echo -e "\033[0m")

VENV_NAME?=.venv
PYTHON=${VENV_NAME}\Scripts\python.exe

setup: ## Activate the virtual environment, creating it if needed
	@if exist $(VENV_NAME) ( \
		echo $(YELLOW)$(VENV_NAME) already created. Skipping package installation.$(RESET) \
	) else ( \
		echo $(GREEN)Creating virtual environment and installing packages...$(RESET) && \
		python -m venv $(VENV_NAME) && \
		$(PYTHON) -m pip install -U pip \
		$(PYTHON) -m pip install -Ur requirements.txt \
	)
	@echo $(GREEN)Starting a sub-shell with the virtual environment activated.$(RESET)

dbt-docs: ##& generate and serve dbt docs locally
	@if [ -d "$(VENV_NAME)" ]; then \
		touch $(VENV_NAME)/bin/activate; \
		dbt docs generate && dbt docs serve; \
	else \
		echo "$(YELLOW)virtual environment not created run make dbt$(RESET)"; \
	fi
	

remake: ## Delete the virtual environment
	rm -rf .venv

help: ## Show targets and comments (must have ##)
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'