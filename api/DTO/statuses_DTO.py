from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from api.DTO import *


class Status(Base):
    __tablename__ = "statuses"

    # Attributes
    status_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Affiliations
    proposal = relationship("Proposal", back_populates="status", foreign_keys=[Proposal.status_id])
    status_history = relationship("StatusHistory", back_populates="status", foreign_keys=[StatusHistory.status_id])

    def __repr__(self):
        return f"<Status id={self.status_id}, name={self.name}, description={self.description}>"
