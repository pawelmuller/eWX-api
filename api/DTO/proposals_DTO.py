from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO.common_DTO import Base, users_units_association_table


class Proposal(Base):
    __tablename__ = "proposals"

    # Attributes
    proposal_id = Column(Integer, primary_key=True)
    reason = Column(String)
    description = Column(String)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("User.user_id"))
    status_id = Column(Integer, ForeignKey("Status.status_id"))

    # Affiliations
    units = relationship("Unit", secondary=users_units_association_table, back_populates="users")
    expenses = relationship("Expense", back_populates="proposal", foreign_keys="[Expense.proposal_id]")
