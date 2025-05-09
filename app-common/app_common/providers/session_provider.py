from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app_common.base_config import BaseConfig

from typing import TypeVar

T = TypeVar("T", bound=BaseConfig)


class AsyncSessionProvider:
    """
    AsyncSessionProvider - is a session provider that lets us create async
    sessions via sqlalchemys asyncio integration.
    """

    def __init__(self, db_url: str, debug: bool = False):
        self._engine = create_async_engine(db_url, echo=debug)
        self._sessionmaker = async_sessionmaker(
            self._engine, expire_on_commit=False)

    @property
    def session(self) -> AsyncSession:
        return self._sessionmaker()


_ASYNC_SESSION_PROVIDER: AsyncSessionProvider | None = None


def create_async_session_provider(config: T) -> AsyncSessionProvider:
    global _ASYNC_SESSION_PROVIDER
    if _ASYNC_SESSION_PROVIDER is not None:
        return _ASYNC_SESSION_PROVIDER
    else:
        _ASYNC_SESSION_PROVIDER = AsyncSessionProvider(
            config.db_url, config.debug)
        return _ASYNC_SESSION_PROVIDER
