cp .env.example .env
docker build . -t django-api-rest
docker run --env-file .env -p 8000:8000 django-api-rest