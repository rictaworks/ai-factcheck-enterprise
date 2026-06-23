import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "production")

app = FastAPI(
    title="AI Factcheck Enterprise - AI Service",
    debug=(APP_ENV == "development"),
)


@app.get("/health")
def health_check():
    return {"status": "ok", "env": APP_ENV}
