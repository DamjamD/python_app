from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Base schema with shared fields
class UserBase(BaseModel):
    user_name: str
    email: EmailStr


# Schema for creating a user
class UserCreate(UserBase):
    password: str  # Field required only during user creation


# Schema for user login
class UserLogin(BaseModel):
    user_name: str
    password: str
    class Config:
        from_attributes = True  # Enables SQLAlchemy model to Pydantic conversion

    


# Schema for updating user details
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None  # Email is optional during updates
    password: Optional[str] = None   # Password is optional during updates


# Schema for user details (output)
class UserDetail(UserBase):
    user_id: int
    created_at: datetime
    last_update: datetime
    user_name: str
    admin: bool

    class Config:
        from_attributes = True  # Enables SQLAlchemy model to Pydantic conversion


# Simplified schema for general user response
class User(UserBase):
    user_id: int
    created_at: datetime
    user_name: str
    is_active: bool  # Include the 'is_active' field to match the database schema

    class Config:
        from_attributes = True
