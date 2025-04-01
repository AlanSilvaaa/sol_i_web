from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    current_time = datetime.now()
    return {"Date and time": current_time}
