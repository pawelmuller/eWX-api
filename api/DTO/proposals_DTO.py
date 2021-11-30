from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO import *


class Proposal(Base):
    __tablename__ = "proposals"

    def __init__(self, user_id, reason, description):
        self.user_id = user_id
        self.reason = reason
        self.description = description
        self.status_id = 1  # ZŁOŻONY

    # Attributes
    proposal_id = Column(Integer, primary_key=True)
    reason = Column(String)
    description = Column(String)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.user_id"))
    status_id = Column(Integer, ForeignKey("statuses.status_id"))

    # Affiliations
    user = relationship("User", back_populates="proposals", foreign_keys=[user_id])
    status = relationship("Status", back_populates="proposal", foreign_keys=[status_id])
    advances = relationship("Advance", back_populates="proposal", foreign_keys=[Advance.proposal_id])
    comments = relationship("Comment", back_populates="proposal", foreign_keys=[Comment.proposal_id])
    expenses = relationship("Expense", back_populates="proposal", foreign_keys=[Expense.proposal_id])
    funding_sources = relationship("FundingSource", back_populates="proposal", foreign_keys=[FundingSource.proposal_id])

    def __repr__(self):
        return f"<Proposal id={self.proposal_id}, reason={self.reason}, desc={self.description}>"
