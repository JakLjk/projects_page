build:
	docker compose build

force-rebuild:
	docker compose build --no-cache

run:
	docker compose up -d

down:
	docker compose down