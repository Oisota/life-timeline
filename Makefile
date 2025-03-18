RUN := uv run

.PHONY: start
start:
	$(RUN) flask run --host=0.0.0.0

.PHONY: lint
lint:
	$(RUN) ruff check --fix

.PHONY: format
format:
	$(RUN) ruff format