
dc = docker-compose

run:
	$(dc) up -d api

run-build:
	$(dc) up -d --build api

setup-db:
	$(dc) run --rm api alembic upgrade head

alembic:
	$(dc) run --rm api alembic revision --autogenerate -m $(msg)
	$(dc) run --rm api alembic upgrade head