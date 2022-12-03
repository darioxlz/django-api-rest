cp .env.example .env
docker build . -t docker-django-api-v0.0
docker run --env-file .env -p 8000:8000 docker-django-api-v0.0