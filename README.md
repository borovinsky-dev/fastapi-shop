# FastAPI Shop

Учебный интернет-магазин на FastAPI. Зависимости и виртуальное окружение проекта управляются через [uv](https://docs.astral.sh/uv/).

## Запуск локально

Требуется Python 3.11 или новее и установленный `uv`.

```powershell
uv sync
Copy-Item .env.example .env
uv run fastapi dev app/main.py
```

`uv sync` создаёт `.venv`, устанавливает основные зависимости и группу разработки, а также поддерживает `uv.lock`. Активировать окружение вручную не нужно: `uv run` использует `.venv` автоматически.

Откройте `http://127.0.0.1:8000/docs` для Swagger UI или `http://127.0.0.1:8000/health` для проверки доступности. По умолчанию используется SQLite; URL базы задаётся в `DATABASE_URL`.

## Зависимости

Основные зависимости: FastAPI, SQLAlchemy, aiosqlite и Alembic. В группе `dev` находятся pytest, pytest-asyncio, httpx и Ruff.

Добавить библиотеку приложения:

```powershell
uv add имя-пакета
```

Добавить инструмент разработки:

```powershell
uv add --dev имя-пакета
```

## Миграции

```powershell
uv run alembic revision --autogenerate -m "initial"
uv run alembic upgrade head
```

Чтобы Alembic видел модели, импортируйте их в `app/models/__init__.py`.

## Запуск с Docker

```sh
docker compose up --build
```

API будет доступно на `http://localhost:8000`; файл SQLite хранится в Docker volume.
