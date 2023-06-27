build:
	docker compose build
up:
	docker compose up

test-nginx-config:
	docker exec stack.nginx nginx -t

reload-nginx-config:
	docker exec stack.nginx nginx -s reload

down:
	docker compose down --remove-orphans