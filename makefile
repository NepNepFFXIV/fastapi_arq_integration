.PHONY: run
run:
	uv run fastapi dev src/fastapi_arq_integration/main.py

.PHONY: ruff
ruff:
	uv run ruff check --fix
	uv run ruff format
