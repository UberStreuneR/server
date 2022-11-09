
dc = docker-compose

run:
	$(dc) up -d api

redis:
	$(dc) up -d redis

uvi:
	uvicorn --reload --port 8000 src.main:app

run-build:
	$(dc) up -d --build api

setup-db:
	$(dc) run --rm api alembic upgrade head

alembic:
	$(dc) run --rm api alembic revision --autogenerate -m $(msg)
	$(dc) run --rm api alembic upgrade head