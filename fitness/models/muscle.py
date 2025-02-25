from sqlmodel import SQLModel, Field
from typing import Optional


class Muscle(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)  # Example: "Biceps", "Quadriceps"
    description: Optional[str] = None
