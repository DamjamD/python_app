from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Base schema for shared attributes
class InsurerBase(BaseModel):
    insurer_name: str

# Schema for creating a new insurer
class InsurerCreate(InsurerBase):
    pass

# Schema for updating an existing insurer
class InsurerUpdate(InsurerBase):
    insurer_name: Optional[str] = None

# Schema for reading an insurer (includes ID and timestamps)
class InsurerRead(InsurerBase):
    insurer_id: int
    created_at: datetime
    insurer_name: str
    class Config:
        from_attributes = True

# Schema for reading an insurer along with associated policies
class InsurerWithPolicies(InsurerRead):
    policies: List["PolicyRead"] = []

    class Config:
        from_attributes = True
