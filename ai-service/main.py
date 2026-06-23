from fastapi import FastAPI

app = FastAPI(title="AI Factcheck Enterprise - AI Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}
