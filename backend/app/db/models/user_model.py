from datetime import datetime, date
from uuid import uuid4
from typing import List, Optional
from pydantic import validator, UUID4
from sqlmodel import Field, SQLModel, Enum


class UserBase(SQLModel):
    username: str
    email: str
    password_hash: Optional[datetime] = Field(default=None)


class User(UserBase, table=True):
    id: Optional[UUID4] = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime
    last_login: datetime
    status: Enum("active", "inactive", "banned")

    @validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or uuid4()
