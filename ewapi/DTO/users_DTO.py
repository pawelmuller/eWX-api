from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from ewapi.DTO import *


class User(Base):
    __tablename__ = "users"

    # Attributes
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    # Relations
    advances = relationship("Advance", back_populates="user", foreign_keys=[Advance.recipient_id])
    chairperson_positions = relationship("Unit", back_populates="chairperson", foreign_keys=[Unit.chairperson_id])
    comments = relationship("Comment", back_populates="user", foreign_keys=[Comment.user_id])
    proposals = relationship("Proposal", back_populates="user", foreign_keys=[Proposal.user_id])
    treasurer_positions = relationship("Unit", back_populates="treasurer", foreign_keys=[Unit.treasurer_id])

    # Affiliations
    units = relationship("Unit", secondary=users_units_association_table, back_populates="users")

    def __repr__(self):
        return f"<User id={self.user_id}, name={self.name}, surname={self.surname}>"
