from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from api.DTO.common_DTO import Base


class Advance(Base):
    __tablename__ = 'advances'

    # Attributes
    recipient_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"), primary_key=True)
    amount = Column(Integer)

    # Affiliations
    user = relationship("User", back_populates="advances", foreign_keys=[recipient_id])
    proposal = relationship("Proposal", back_populates="advances", foreign_keys=[proposal_id])
