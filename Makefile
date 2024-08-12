APP_NAME:=digits_predictor

up:
	docker-compose up -d --build

down:
	docker-compose down --remove-orphans