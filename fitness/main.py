from fastapi import FastAPI

from fitness.config.settings import Settings

app = FastAPI()


@app.get("/")
async def health_check():
    return {"status": "ok"}


@app.get("/settings")
async def get_settings():
    return Settings().model_dump()
