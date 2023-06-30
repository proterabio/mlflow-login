build:
	docker compose build

up:
	docker compose up

test-nginx-config:
	docker exec stack.nginx nginx -t

reload-nginx-config:
	docker exec stack.nginx nginx -s reload

e2e:
	docker exec stack.flask pytest tests/e2e

integration:
	docker exec stack.flask pytest tests/integration

unit:
	docker exec stack.flask pytest tests/unit

test:
	unit integration e2e

down:
	docker compose down --remove-orphans
