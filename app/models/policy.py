from sqlalchemy import Column, Integer, Float, Date, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(Integer, primary_key=True, index=True)              # Unique identifier for the policy
    created_at = Column(DateTime, default=func.now(), nullable=False)  # Creation timestamp
    transmition_date = Column(DateTime, nullable=False)
    start_date = Column(Date, nullable=False, index=True)                 # Policy start date
    end_date = Column(Date, nullable=False, index=True)                   # Policy end date
    gross_commission = Column(Float, nullable=False)                      # Gross commission
    store_commission = Column(Float, nullable=True)                       # Store commission
    commission_rate = Column(Float, nullable=True)                        # Commission percentage
    customer_name = Column(String(255), nullable=False, index=True)
    last_update = Column( DateTime, default=func.now(), onupdate=func.now())

    # Foreign Keys
    insurer_id = Column(Integer, ForeignKey("insurers.insurer_id"), nullable=False)  # Associated insurer
    created_by_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False) # User who created the policy

    # Relationships
   # insurer = relationship("Insurer", back_populates="policies")          # Link to Insurer model
   # created_by = relationship("User", back_populates="policies")          # Link to User model

    #def __repr__(self):
    #    return f"<Policy(policy_id={self.policy_id}, start_date={self.start_date}, end_date={self.end_date}, insurer_id={self.insurer_id}, created_by_user_id={self.created_by_user_id})>"
