from datetime import datetime, date
from uuid import uuid4
from typing import List, Optional, TYPE_CHECKING
from pydantic import validator, UUID4
from sqlmodel import Field, SQLModel, ARRAY, String, Column, Text
from user_model import User

if TYPE_CHECKING:
    from .user_model import User

class EventBase(SQLModel):
    name: str
    link: str
    description: Text
    date: Optional[datetime] = Field(default=None)
    address: str
    city: str
    country: str
    genre: List[str] = Field(sa_column=Column(ARRAY(String)))
    format: List[str] = Field(sa_column=Column(ARRAY(String)))
    reg_start: Optional[datetime] = Field(default=None)
    reg_end: Optional[datetime] = Field(default=None)


class Event(EventBase, table=True):
    id: Optional[UUID4] = Field(default_factory=uuid4, primary_key=True)
    organizer_id: UUID4 | None = Field(default=None, foreign_key="user.id")   
    
    @validator('id', pre=True, always=True)
    def default_id(cls, v):
        return v or uuid4()
