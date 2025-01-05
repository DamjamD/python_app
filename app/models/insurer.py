from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Insurer(Base):
    __tablename__ = "insurers"

    insurer_id = Column(Integer, primary_key=True, index=True)
    insurer_name = Column(String(255), nullable=False, unique=True, index=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    is_active = Column(Boolean, default=True)
    last_update = Column( DateTime, default=func.now(), onupdate=func.now())

    #policies = relationship("Policy", back_populates="insurer")  # Link to policies

    def __repr__(self):
        return f"<Insurer(insurer_id={self.insurer_id}, name='{self.insurer_name}')>"
