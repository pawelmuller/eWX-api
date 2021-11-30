from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, TIMESTAMP
from api.DTO import *


class StatusHistory(Base):
    __tablename__ = "status_history"

    # Attributes
    status_history_id = Column(Integer, primary_key=True)
    time = Column(TIMESTAMP)

    # Foreign keys
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"))
    status_id = Column(Integer, ForeignKey("statuses.status_id"))

    # Relations
    proposal = relationship("Proposal", foreign_keys=[proposal_id])
    status = relationship("Status", back_populates="status_history", foreign_keys=[status_id])

    def __repr__(self):
        return f"<StatusHistory id={self.status_history_id}, time={self.time}, status={self.status}>"
