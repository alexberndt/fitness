from __future__ import annotations

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from fitness.models.user import User
from fitness.models.exercise import Exercise


class Log(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    exercise_id: int = Field(foreign_key="exercise.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="logs")
    exercise: "Exercise" = Relationship()
