from pydantic import BaseModel


class Muscle(BaseModel):
    id: str
    name: str


class Exercise(BaseModel):
    id: str
    name: str
    description: str
    target_muscles: list[Muscle]
