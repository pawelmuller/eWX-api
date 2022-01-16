from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from ewapi.DTO import *


class Expense(Base):
    __tablename__ = "expenses"

    # Attributes
    expense_id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    type = Column(String)

    # Foreign keys
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"))

    # Relations
    proposal = relationship("Proposal", back_populates="expenses", foreign_keys=[proposal_id], lazy='subquery')

    def __repr__(self):
        return f"<Expense id={self.expense_id}, name={self.name}, type={self.type}, price={self.quantity}x{self.price}>"
