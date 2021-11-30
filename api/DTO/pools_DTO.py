from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from api.DTO import *


class Pool(Base):
    __tablename__ = "pools"

    # Attributes
    year = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey("units.unit_id"), primary_key=True)
    budget = Column(Integer)

    # Affiliations
    unit = relationship("Unit", back_populates="pools", foreign_keys=[unit_id])

    def __repr__(self):
        return f"<Pool year={self.year}, budget={self.budget}, unit={self.unit}>"
