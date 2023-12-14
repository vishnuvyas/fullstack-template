"""
Test App Backend

Tests wether the basic import works for the app_backend.
"""
from app_backend.__main__ import app
from unittest import TestCase


class TestAppBackend(TestCase):

    def test_app(self):
        self.assertIsNotNone(app)
