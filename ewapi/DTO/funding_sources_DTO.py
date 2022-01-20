from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from ewapi.DTO import *


class FundingSource(Base):
    __tablename__ = "funding_sources"

    def __init__(self, proposal_id, pool_id, amount):
        self.proposal_id = proposal_id
        self.pool_id = pool_id
        self.amount = amount

    # Attributes
    amount = Column(Integer)

    # Foreign keys
    pool_id = Column(Integer, ForeignKey("pools.pool_id"), primary_key=True)
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"), primary_key=True)

    # Relations
    pools = relationship("Pool", back_populates="funding_sources", foreign_keys=[pool_id])
    proposal = relationship("Proposal", back_populates="funding_sources", foreign_keys=[proposal_id])

    def __repr__(self):
        return f"<FundingSource id={self.funding_source_id}, amount={self.amount}>"
