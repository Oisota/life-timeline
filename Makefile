RUN := uv run

.PHONY: start
start:
	$(RUN) flask run --host=0.0.0.0

.PHONY: lint
lint:
	$(RUN) ruff check --select I --fix

.PHONY: format
format:
	$(RUN) ruff format

.PHONY: test
test:
	$(RUN) pytest