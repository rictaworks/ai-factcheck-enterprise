import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "production")
APP_TITLE = os.getenv("APP_TITLE", "AI Factcheck Enterprise - AI Service")

app = FastAPI(
    title=APP_TITLE,
    debug=(APP_ENV == "development"),
)


@app.get("/health")
def health_check():
    return {"status": "ok", "env": APP_ENV}
