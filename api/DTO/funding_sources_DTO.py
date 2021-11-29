from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String
from api.DTO.common_DTO import Base


class FundingSource(Base):
    __tablename__ = "funding_sources"

    # Attributes
    funding_source_id = Column(Integer, primary_key=True)
    amount = Column(Integer)

    # Foreign keys
    unit_id = Column(Integer, ForeignKey("units.unit_id"))

    # Relations
    units = relationship("Unit", back_populates="funding_sources", foreign_keys=[unit_id])
