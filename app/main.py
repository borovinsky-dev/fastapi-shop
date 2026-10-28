from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import db_session

# перед запуском приложения используется asynccontextmanager,
# чтобы открыть подключение к базе данных, а также для чистки ресурсов


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Run shop-app")
    yield
    print("Stop shop-app")
    await db_session.dispose()


app = FastAPI(title="shop-app", lifespan=lifespan)
