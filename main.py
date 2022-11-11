from fastapi import FastAPI
import uvicorn
from mylibrary.logic import search_wiki as wikisearch
from mylibrary.logic import wiki as wikiintro
from mylibrary.logic import phrase as wikiphrases

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "This is a Wikipedia API. Please call: /search or /wiki or /phrase"
    }

@app.get("/search/{value}")
async def search(value: str):
    """Page to search something you are interested in at wikipedia"""

    result = wikisearch(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve the basic introduction at wikipedia"""

    result = wikiintro(name)
    return {"result": result}

@app.get("/phrase/{name}")
async def phrase(name: str):
    """Return related phrases at wikipedia"""

    result = wikiphrases(name)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
