from datetime import datetime, date
from uuid import uuid4
from typing import List, Optional, TYPE_CHECKING
from pydantic import validator, UUID4
from sqlmodel import Field, SQLModel, ARRAY, String, Column, Text, Relationship
from ..db.models.profile_model import ProfileBase


class ProfileCreate(ProfileBase):
    pass


class ProfileRead(ProfileBase):
    id: UUID4


class ProfileUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    dob: Optional[datetime] = None
    profile_photo: str # url
    city: Optional[str] = None
    country: Optional[str] = None
