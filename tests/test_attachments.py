import pytest
from sqlalchemy.exc import IntegrityError

from ewapi import CRUD
from ewapi.utils.db_connection import create_db_engine, get_session


class TestAttachment:
    def test_add_attachment(self):
        create_db_engine(test=True)
