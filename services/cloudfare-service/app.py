from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"service": "user-service", "status": "running"}
