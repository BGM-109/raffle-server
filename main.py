from fastapi import FastAPI
import json
from datetime import date
import pandas as pd


app = FastAPI()

t_date = date.today().strftime("%y%m%d")
t_filename = f"{t_date}.csv"





@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/raffle")
async def get_raffle():
    try:
        df = pd.read_csv(t_filename)
        res = df.to_json(orient="records")
        parsed = json.loads(res)
    except:
        parsed = {"error" : "오늘의 데이터가 없습니다." }
    return parsed
    
    