from __future__ import annotations

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class ExerciseMuscleLink(SQLModel, table=True):
    exercise_id: int = Field(foreign_key="exercise.id", primary_key=True)
    muscle_id: int = Field(foreign_key="muscle.id", primary_key=True)


class Exercise(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)  # Example: "Bench Press"
    description: Optional[str] = None
    sets: Optional[int] = None
    repetitions: Optional[int] = None

    target_muscles: List["Muscle"] = Relationship(  # noqa: F821
        back_populates="exercises", link_model=ExerciseMuscleLink
    )
