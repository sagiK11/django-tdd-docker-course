docker-compose exec movies flake8 .
docker-compose exec movies black --exclude=migrations .
docker-compose exec movies isort .