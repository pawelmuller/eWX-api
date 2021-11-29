from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO.common_DTO import Base


class Expense(Base):
    __tablename__ = "expenses"

    # Attributes
    expense_id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    type = Column(String)

    # Foreign keys
    proposal_id = Column(Integer, ForeignKey("Proposal.proposal_id"))

    # Relations
    proposal = relationship("Proposal", back_populates="expenses", foreign_keys=[proposal_id])
