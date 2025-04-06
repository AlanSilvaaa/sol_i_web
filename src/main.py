from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/time")


@app.get("/time")
async def time():
    current_time = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    return {"Date and time": current_time}
