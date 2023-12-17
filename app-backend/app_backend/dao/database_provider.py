from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os


class DatabaseProvider:

    def __init__(self, db_url: str = os.getenv("DB_URL", "sqlite:///:memory:"), testing: bool = False):
        self.db_url = db_url
        self.testing = testing
        if self.testing:
            self._engine = create_engine(self.db_url, echo=True,
                                         connect_args={'check_same_thread': False})
        else:
            self._engine = create_engine(self.db_url, echo=False)

        self._session_maker = sessionmaker(bind=self._engine)

    @property
    def engine(self):
        return self._engine

    def session(self):
        if self._session_maker:
            return self._session_maker()
        else:
            raise ValueError(
                "Database has already been disposed, create a new instance.")

    def dispose(self):
        self._engine.dispose()
        self._engine = None
        self._session_maker = None

    def create_all(self, metadata: MetaData):
        metadata.create_all(bind=self._engine)

    def drop_all(self, metadata: MetaData):
        metadata.drop_all(bind=self._engine)


@contextmanager
def DBProvider(db_url: str = os.getenv("DB_URL", "sqlite:///:memory:"), testing: bool = False):
    db_provider = DatabaseProvider(db_url, testing)
    yield db_provider
    db_provider.dispose()
