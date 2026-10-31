from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import text

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


# проверка подключения к БД
@app.get("/health/db")
async def health_db(session: AsyncSession = Depends(db_session.get_session)):
    await session.execute(text("Select 1"))
    return {"status": "ok", "database": "connected"}
