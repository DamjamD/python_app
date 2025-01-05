from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional

# Base schema for shared attributes
class PolicyBase(BaseModel):
    start_date: date
    end_date: date
    gross_commission: float
    store_commission: Optional[float] = None
    commission_rate: Optional[float] = None
    transmition_date: Optional[date] = None
    customer_name: str
   

# Schema for creating a new policy
class PolicyCreate(PolicyBase):
     class Config:
        from_attributes = True


# Schema for updating an existing policy
class PolicyUpdate(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    gross_commission: Optional[float] = None
    store_commission: Optional[float] = None
    commission_rate: Optional[float] = None
    insurer_id: Optional[int] = None
    created_by_user_id: Optional[int] = None
    transmition_date: Optional[date] = None
    customer_name: Optional[str] =None

# Schema for reading a policy (includes ID and timestamps)
class PolicyRead(PolicyBase):
    policy_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Schema for reading a policy with related data
class PolicyWithDetails(PolicyRead):
    insurer: "InsurerRead"
    created_by: "UserRead"

    class Config:
        from_attributes = True
