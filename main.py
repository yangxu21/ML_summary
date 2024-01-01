import uvicorn
from fastapi.responses import JSONResponse
from fastapi. encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.bot import scrape

app = FastAPI()

class Wiki(BaseModel):
    name: str

@app.post("/wiki")
async def scrape_story(wiki: Wiki):
    result = scrape(name=wiki.name)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Helxlo Functions"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

if __name__=='__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
