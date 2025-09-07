from typing import List, Optional
import reflex as rx
import sqlmodel
from sqlmodel import Field, Relationship 
import datetime

import reflex_local_auth   # Importing LocalUser model for user management
#from reflex_local_auth.user import LocalUser
# Define the UserRole model for managing user roles

class User_Role(rx.Model, table=True): 
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False)  # Role name, e.g., 'admin', 'user'
    description: str = Field(nullable=True)  # Optional description of the role

    userinfo: List["UserInfo"] = Relationship(back_populates="user_role")  # Relationship to UserInfo model

class PasswordResetToken(rx.Model, table=True):
    user_id: int = Field(foreign_key="localuser.id") # Foreign key to the User model
    token: str # Unique token for password reset
    expires_at: datetime.datetime  # Expiration time for the token

class UserInfo(rx.Model, table=True):    
    user_id: int = Field(foreign_key="localuser.id", ondelete="CASCADE")  # Foreign key to the User model
    role_id: int = Field(foreign_key="user_role.id")  # Foreign key to the Role model
    name: str = Field(nullable=True)  # Optional name field
    email: str = Field(unique=True, index=True)  # Unique email address
    phone: str = Field(nullable=True)  # Optional phone number
    is_admin: bool = False # Default to False, can be set to True for admin users

    localuser: Optional["reflex_local_auth.LocalUser"] = Relationship()  # Relationship to the LocalUser model
    user_role: Optional["User_Role"] = Relationship(back_populates="userinfo")  # Relationship to the User_Role model
    