build:
	docker compose build

force-rebuild:
	docker compose build --no-cache

run:
	docker compose up -d
	
run-rebuild:
	docker compose up --build -d
down:
	docker compose down