from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO import *


class Unit(Base):
    __tablename__ = 'units'

    # Attributes
    unit_id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    description = Column(String)

    # Foreign keys
    chairperson_id = Column(Integer, ForeignKey("users.user_id"))
    treasurer_id = Column(Integer, ForeignKey("users.user_id"))

    # Relations
    chairperson = relationship("User", back_populates="chairperson_positions", foreign_keys=[chairperson_id])
    treasurer = relationship("User", back_populates="treasurer_positions", foreign_keys=[treasurer_id])

    # Affiliations
    users = relationship("User", secondary=users_units_association_table, back_populates="units")
    funding_sources = relationship("FundingSource", back_populates="unit", foreign_keys="[FundingSource.unit_id]")
    pools = relationship("Pool", back_populates="unit", foreign_keys="[Pool.unit_id]")

    def __repr__(self):
        return f"<Unit id={self.unit_id}, type={self.type}, name={self.name}>"