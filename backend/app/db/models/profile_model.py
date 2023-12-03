from datetime import datetime, date
from uuid import uuid4
from typing import List, Optional, TYPE_CHECKING
from pydantic import validator, UUID4
from sqlmodel import Field, SQLModel, ARRAY, String, Column, Text, Relationship

if TYPE_CHECKING:
    from .user_model import User


class ProfileBase(SQLModel):
    first_name: str
    last_name: str
    bio: Text
    dob: Optional[datetime] = Field(default=None)
    profile_photo: str # url
    city: str
    country: str


class Profile(ProfileBase, table=True):
    id: Optional[UUID4] = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID4 | None = Field(default=None, foreign_key="user.id")

    @validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or uuid4()
    