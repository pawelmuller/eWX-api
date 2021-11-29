from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO.common_DTO import Base


class Proposal(Base):
    __tablename__ = "proposals"

    # Attributes
    proposal_id = Column(Integer, primary_key=True)
    reason = Column(String)
    description = Column(String)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.user_id"))
    status_id = Column(Integer, ForeignKey("statuses.status_id"))

    # Affiliations
    user = relationship("User", back_populates="proposals", foreign_keys=[user_id])
    status = relationship("Status", back_populates="proposals", foreign_keys=[status_id])
    advances = relationship("Advance", back_populates="proposal", foreign_keys="[Advance.proposal_id]")
    comments = relationship("Comment", back_populates="proposal", foreign_keys="[Comment.proposal_id]")
    expenses = relationship("Expense", back_populates="proposal", foreign_keys="[Expense.proposal_id]")
