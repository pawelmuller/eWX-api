from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *


class User(declarative_base()):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    unit_id = Column(Integer)
