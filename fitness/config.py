from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str = "localhost"
    db_name: str
    db_port: int

    class Config:
        env_file = ".env.example"  # Optional: Loads values from a .env file if present


# Create an instance of the settings
settings = Settings()
