from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, LargeBinary
from ewapi.DTO import *


class Attachment(Base):
    __tablename__ = 'attachments'

    def __init__(self, attachment_id, proposal_id, filename, file_content):
        self.attachment_id = attachment_id
        self.proposal_id = proposal_id
        self.filename = filename
        self.file_content = file_content

    # Attributes
    proposal_id = Column(Integer, ForeignKey("proposals.proposal_id"), primary_key=True)
    attachment_id = Column(Integer, primary_key=True)
    filename = Column(String)
    file_content = Column(LargeBinary)

    # Relations
    proposal = relationship("Proposal", back_populates="attachments", foreign_keys=[proposal_id], lazy="subquery")

    def __repr__(self):
        return f"<Attachment id={self.attachment_id}, filename={self.filename}>"
