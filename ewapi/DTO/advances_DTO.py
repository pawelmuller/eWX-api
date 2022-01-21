from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from ewapi.DTO import *


class Advance(Base):
    __tablename__ = 'advances'

    def __init__(self, recipient_id, proposal_id, amount):
        self.recipient_id = recipient_id
        self.proposal_id = proposal_id
        self.amount = amount

    # Attributes
    recipient_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"), primary_key=True)
    amount = Column(Integer)

    # Relations
    user = relationship("User", back_populates="advances", foreign_keys=[recipient_id])
    proposal = relationship("Proposal", back_populates="advances", foreign_keys=[proposal_id])

    def __repr__(self):
        return f"<Advance user={self.user}, proposal={self.proposal}, amount={self.amount}>"
