RUN := uv run

.PHONY: start
start:
	$(RUN) flask run --host=0.0.0.0