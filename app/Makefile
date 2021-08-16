.PHONY: app


HERE := ${CURDIR}

CONTAINER := playground_celery

build:
	cd conf\app && docker build -t ${CONTAINER} -f Dockerfile.app .

run:
	docker run  --hostname docker -v ${HERE}/workspace:/workspace -it ${CONTAINER}


up:
	docker compose up -d

up-with-build:
	docker compose up -d --build

down:
	docker compose down

broker_up:
	docker compose up broker -d

broker:
	docker compose exec broker /bin/bash

worker_up:
	docker compose up worker -d

worker:
	docker compose exec worker /bin/bash

flower_up:
	docker compose up flower -d

flower:
	docker compose exec flower /bin/bash

app_up:
	docker compose up app -d

app:
	docker compose exec app /bin/bash

		