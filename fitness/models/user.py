from sqlmodel import SQLModel, Field, Relationship
from typing import List


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password: str

    logs: List["Log"] = Relationship(back_populates="user")
