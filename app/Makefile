.PHONY: app


HERE := ${CURDIR}

CONTAINER := playground_celery

build:
	docker build -t ${CONTAINER} .

run:
	docker run  --hostname docker -v ${HERE}/workspace:/workspace -it ${CONTAINER}


up:
	docker compose up -d

down:
	docker compose down


brokser_up:
	docker compose up broker -d

broker:
	docker compose exec broker /bin/bash

app:
	docker compose exec app /bin/bash

		