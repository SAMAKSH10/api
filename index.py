from fastapi import *
from fastapi.params import Body

app=FastAPI()
@app.get("/")
async def add(num1,num2):
    result=num1+num2
    return {"Sum":result}
