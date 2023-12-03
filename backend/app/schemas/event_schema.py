from datetime import datetime, date
from uuid import uuid4
from typing import List, Optional
from pydantic import validator, UUID4
from sqlmodel import Field, SQLModel, ARRAY, String, Column, Text
from ..db.models.event_model import EventBase


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: UUID4


class EventReadAll(SQLModel):
    id: Optional[UUID4] = None
    name: Optional[str] = None
    date: Optional[datetime] = None
    city: Optional[str] = None
    country: Optional[str] = None
    genre: Optional[List[str]] = None
    format: Optional[List[str]] = None


class EventUpdate(SQLModel):
    name: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None
    genre: Optional[List[str]] = None
    format: Optional[List[str]] = None
    country: Optional[str] = None
    address: Optional[str] = None
    reg_start: Optional[date] = None
    reg_end: Optional[date] = None
