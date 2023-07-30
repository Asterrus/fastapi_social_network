### Описание
   Сервис реализован на FastAPI.  
   База данных - PostgreSQL  
   ORM - SQLAlchemy, миграции - Alembic  
   Проект разворачивается с помощью docker compose   
   Python версии 3.11.1  
   Хранение лайков пользователей и токенов в Redis.
### Технологии:
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FastAPI](https://img.shields.io/badge/FastAPI-092E20?style=for-the-badge&logo=FastAPI&logoColor=green)
![Docker](https://img.shields.io/badge/Docker-092E20?style=for-the-badge&logo=docker&logoColor=blue)
### Используемые пакеты:
* aiohttp==3.8.5
* alembic==1.11.1
* asyncpg==0.28.0
* SQLAlchemy==2.0.19
* uvicorn==0.23.1
* fastapi==0.100.1
* fastapi-users==12.1.0
* fastapi-users-db-sqlalchemy==6.0.0
* redis==4.6.0
* pydantic==2.1.1
* python-dotenv==1.0.0

### Установка

1. Клонировать репозиторий:

   ```python
   git clone ...
   ```

2. Перейти в папку с проектом:

   ```python
   cd fastapi_social_network/backend/
   ```
3. Добавить переменные окружения:
   ```
   touch .env
   Добавить в файл .env данные:
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   # Если планируется использовать верификацию email hunter api:
   USE_HUNTER_URL=True
   HUNTER_URL=https://api.hunter.io/v2/email-verifier
   HUNTER_IO_API_KEY=API_KEY # Подставить свой api_key
   ```
5. Создать и запустить контейнер:

   ```python
   docker-compose up -d
   ```
### Дополнительно

* Ресурс доступен по адресу:
   ```
   http://127.0.0.1:8000
   ```
* Документация:
   ```
   http://127.0.0.1:8000/docs
   ```
### Пример запроса
* Регистрация пользователя.
    `POST http://127.0.0.1:8000/auth/register`
* Пример запроса:
    ```json
    {
      "email": "user_test@example.com",
      "password": "string"
    }
    ```
* Пример ответа:
    ```json
    {
      "id": 3,
      "email": "user_test@example.com",
      "is_active": true,
      "is_superuser": false,
      "is_verified": false,
      "first_name": null,
      "last_name": null,
      "birthdate": null,
      "register_at": "2023-07-30T23:10:48.765415",
      "updated_at": "2023-07-30T23:10:48.765415",
      "posts": []
    }
    ```
* Авторизация пользователя.
    `POST http://127.0.0.1:8000/auth/login`
* Пример запроса:
    Content-Type: application/x-www-form-urlencoded
    payload: username=user_test@example.com&password=string
* Пример ответа:
    ```json
    {
        "access_token": "IWKY1NKvJLwM-yQv1tz1lQni-4NnpXKIZn_qP2G1r7w",
        "token_type": "bearer"
    }
    ```
* Создание поста. Нужен токен.
    `POST http://127.0.0.1:8000/posts/create`
* Пример запроса:
   ```json
    {
      "title": "string",
      "content": "string"
    }
  ```
* Пример ответа:
    ```json
    {
      "id": 2,
      "created_at": "2023-07-30T23:30:21.472415",
      "title": "string",
      "content": "string",
      "author_id": 3
    }
    ```
### Автор проекта 
* Роман Дячук   



