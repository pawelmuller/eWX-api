from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from api.DTO import *


class FundingSource(Base):
    __tablename__ = "funding_sources"

    # Attributes
    funding_source_id = Column(Integer, primary_key=True)
    amount = Column(Integer)

    # Foreign keys
    unit_id = Column(Integer, ForeignKey("units.unit_id"))
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"))

    # Relations
    unit = relationship("Unit", back_populates="funding_sources", foreign_keys=[unit_id])
    proposal = relationship("Proposal", back_populates="funding_sources", foreign_keys=[proposal_id])

    def __repr__(self):
        return f"<FundingSource id={self.funding_source_id}, amount={self.amount}>"
