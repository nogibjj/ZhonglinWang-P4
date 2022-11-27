from fastapi import FastAPI
import uvicorn
from mylibrary.logic import arxiv


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "This is a Wikipedia API. Please call: /search or /wiki or /phrase"
    }

@app.get("/arx/{name}")
async def arxivscraper(name: str):
    """Retrieve the basic introduction at Arxiv"""
    result = arxiv(name)
    return {"result": result}


"""Search for something you are interested at Arxiv"""
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
