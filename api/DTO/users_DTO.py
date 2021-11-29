from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from api.DTO.common_DTO import Base, users_units_association_table


class User(Base):
    __tablename__ = "users"

    # Attributes
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    # Relations
    chairperson_positions = relationship("Unit", back_populates="chairperson", foreign_keys="[Unit.chairperson_id]")
    treasurer_positions = relationship("Unit", back_populates="treasurer", foreign_keys="[Unit.treasurer_id]")

    # Affiliations
    units = relationship("Unit", secondary=users_units_association_table, back_populates="users")
    proposals = relationship("Proposal", back_populates="user", foreign_keys="[Proposal.user_id]")
    advances = relationship("Advance", back_populates="user", foreign_keys="[Advance.recipient_id]")
    comments = relationship("Comment", back_populates="user", foreign_keys="[Comment.user_id]")
