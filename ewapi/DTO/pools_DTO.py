from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from ewapi.DTO import *


class Pool(Base):
    __tablename__ = "pools"

    def __init__(self, pool_id: int, year: int, budget: int, unit_id: int):
        self.pool_id = pool_id
        self.year = year
        self.budget = budget
        self.unit_id = unit_id

    # Attributes
    pool_id = Column(Integer, primary_key=True)
    year = Column(Integer)
    budget = Column(Integer)

    # Foreign keys
    unit_id = Column(Integer, ForeignKey("units.unit_id"), primary_key=True)

    # Relations
    unit = relationship("Unit", back_populates="pools", foreign_keys=[unit_id], lazy="subquery")
    funding_sources = relationship("FundingSource", back_populates="pools", foreign_keys=[FundingSource.pool_id], lazy="subquery")

    def __repr__(self):
        return f"<Pool id={self.pool_id}, year={self.year}, budget={self.budget}, unit={self.unit}>"
