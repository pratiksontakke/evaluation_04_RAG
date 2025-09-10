from fastapi import FastAPI
from fastapi.responses import RedirectResponse
app = FastAPI()

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
    return {"status": "ok"}