from asyncio import current_task
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, async_scoped_session

from app.core import settings


class DataBase:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()

database = DataBase(
    url=settings.db_url,
    echo=settings.DB_ECHO
)
