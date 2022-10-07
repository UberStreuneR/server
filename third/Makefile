# also include the Docker Compose file of the VSCode config to avoid warnings about orphaned services
dc = docker-compose -f ./backend-compose.yml -f ./frontend-compose.yml
user_id:=1001
# user_id:=$(shell id -u)
group_id:=1001
# group_id:=$(shell id -g)

build:
	docker build ./backend -t orders_api --build-arg USER_ID=$(user_id) --build-arg GROUP_ID=$(group_id)

setup-db:
	$(dc) up -d db
	timeout 5
	$(dc) run --rm api alembic upgrade head

run:
	$(dc) up -d api
	$(dc) up -d nginx

run-front:
	$(dc) up -d client

run-front-rebuild:
	$(dc) up --build -d client

delete-db:
	$(dc) stop db
	$(dc) rm -v db
	$(dc) up -d db
	sleep 2

recreate-db: delete-db setup-db

insert-mockdata:
	$(dc) run --rm api python -m orders_api.mock

compile-requirements:
	$(dc) run --rm api bash -c "\
		python -m pip install pip-tools && \
		pip-compile -U -o requirements/requirements.txt && \
		pip-compile -U requirements/test-requirements.in -o requirements/test-requirements.txt"

alembic-revision:
	$(dc) run --rm api alembic revision --autogenerate -m $(msg)

logs:
	$(dc) logs -f

insert-mockdata:
	$(dc) run --rm api python -m orders_api.mock

test:
	$(dc) run --rm -e POSTGRES_DB="order_api_testdb" api python -m pytest tests -sv