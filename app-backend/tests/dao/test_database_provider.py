from unittest import TestCase
from app_backend.dao.database_provider import DBProvider


class TestDBProvider(TestCase):

    def test_db_provider(self):
        with DBProvider(testing=True) as provider:
            self.assertIsNotNone(provider)
            with provider.session() as session:
                self.assertIsNotNone(session)
