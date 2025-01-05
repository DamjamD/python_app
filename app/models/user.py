from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    last_update = Column( DateTime, default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)

    # String-based relationship reference
    #policies = relationship("Policy", back_populates="created_by")
