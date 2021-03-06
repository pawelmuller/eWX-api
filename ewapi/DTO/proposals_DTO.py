from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from ewapi.DTO import *
from ewapi.DTO.attachments_DTO import Attachment


class Proposal(Base):
    __tablename__ = "proposals"

    def __init__(self, proposal_id, user_id, name, description, status_id):
        self.proposal_id = proposal_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.status_id = status_id

    # Attributes
    proposal_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.user_id"))
    status_id = Column(Integer, ForeignKey("statuses.status_id"))

    # Relations
    advances = relationship("Advance", back_populates="proposal", foreign_keys=[Advance.proposal_id], lazy="joined")
    comments = relationship("Comment", back_populates="proposal", foreign_keys=[Comment.proposal_id], lazy="joined")
    expenses = relationship("Expense", back_populates="proposal", foreign_keys=[Expense.proposal_id], lazy="joined")
    attachments = relationship("Attachment", back_populates="proposal", foreign_keys=[Attachment.proposal_id])
    funding_sources = relationship("FundingSource", back_populates="proposal", foreign_keys=[FundingSource.proposal_id], lazy="joined")
    status = relationship("Status", back_populates="proposal", foreign_keys=[status_id], lazy="joined")
    user = relationship("User", back_populates="proposals", foreign_keys=[user_id], lazy="joined")

    def __repr__(self):
        return f"<Proposal id={self.proposal_id}, name={self.name}, desc={self.description}>"
