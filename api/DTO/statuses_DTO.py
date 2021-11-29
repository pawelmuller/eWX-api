from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO.common_DTO import Base


class Status(Base):
    __tablename__ = "statuses"

    # Attributes
    status_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Foreign keys
    proposal_id = Column(Integer, ForeignKey("Proposal.proposal_id"))

    # Affiliations
    proposal = relationship("Proposal", back_populates="expenses", foreign_keys=[proposal_id])
