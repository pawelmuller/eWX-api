from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO.common_DTO import Base, users_units_association_table


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
