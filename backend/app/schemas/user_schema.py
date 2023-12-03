from datetime import datetime, date
from uuid import uuid4
from typing import List, Optional
from pydantic import validator, UUID4
from sqlmodel import Field, SQLModel
from ..db.models.user_model import UserBase


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: UUID4


class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
