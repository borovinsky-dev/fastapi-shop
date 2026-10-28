from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


class AsyncDatabaseSession:
    def __init__(
        self,
        database_url: str = settings.DATABASE_URL,
    ) -> None:
        self.engine = create_async_engine(url=database_url)
        # фабрика создания сессий
        self.session_factory = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
        )

    # для создания новой сессии, в которой выполняются асинхронные действия
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        async with self.session_factory() as session:
            yield session

    async def dispose(self) -> None:
        await self.engine.dispose()


# создает подключение к БД и фабрика сессий
db_session = AsyncDatabaseSession()
