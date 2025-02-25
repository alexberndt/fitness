from sqlmodel import SQLModel, create_engine

from fitness.config import settings


# Create a database engine
url = f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
engine = create_engine(url, echo=True)


# Function to initialize database
def init_db():
    from fitness.models.user import User  # noqa
    from fitness.models.exercise import Exercise  # noqa
    from fitness.models.log import Log  # noqa
    from fitness.models.muscle import Muscle  # noqa

    SQLModel.metadata.create_all(engine)
