from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, TIMESTAMP
from api.DTO.common_DTO import Base


class Comment(Base):
    __tablename__ = "comments"

    # Attributes
    comment_id = Column(Integer, primary_key=True)
    content = Column(String)
    time = Column(TIMESTAMP)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.user_id"))
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"))

    # Affiliations
    user = relationship("User", back_populates="comments", foreign_keys=[user_id])
    proposal = relationship("Proposal", back_populates="comments", foreign_keys=[proposal_id])
