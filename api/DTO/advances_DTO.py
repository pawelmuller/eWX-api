from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from api.DTO import *


class Advance(Base):
    __tablename__ = 'advances'

    # Attributes
    recipient_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"), primary_key=True)
    amount = Column(Integer)

    # Relations
    user = relationship("User", back_populates="advances", foreign_keys=[recipient_id])
    proposal = relationship("Proposal", back_populates="advances", foreign_keys=[proposal_id])

    def __repr__(self):
        return f"<Advance user={self.user}, proposal={self.proposal}, amount={self.amount}>"
