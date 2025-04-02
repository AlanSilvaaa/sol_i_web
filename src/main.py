from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"Go to the /time tab"}

@app.get("/time")
async def time():
    current_time = datetime.now()
    return {"Date and time": current_time}
