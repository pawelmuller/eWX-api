from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Table, Column

Base = declarative_base()

users_units_association_table = Table('affiliation', Base.metadata,
                                      Column('user_id', ForeignKey('users.user_id'), primary_key=True),
                                      Column('unit_id', ForeignKey('units.unit_id'), primary_key=True)
                                      )
