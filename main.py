from fastapi import FastAPI
import uvicorn
from mylibrary.logic import arxiv


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "This is a Arxiv API. Call: /docs or /arx/{categories you search}",
        "Computer Science": "cs",
        "Economics": "econ",
        "Electrical Engineering and Systems Science":"eess",
        "Mathematics":"math",
        "Physics":	"physics",
        "Astrophysics":	"physics:astro-ph",
        "Condensed Matter":	"physics:cond-mat",
        "General Relativity and Quantum Cosmology":	"physics:gr-qc",
        "High Energy Physics - Experiment":	"physics:hep-ex",
        "High Energy Physics - Lattice":"physics:hep-lat",
        "High Energy Physics - Phenomenology":"physics:hep-ph",
        "High Energy Physics - Theory":"physics:hep-th",
        "Mathematical Physics":"physics:math-ph",
        "Nonlinear Sciences":"physics:nlin",
        "Nuclear Experiment":"physics:nucl-ex",
        "Nuclear Theory":"physics:nucl-th",
        "Physics (Other)":"physics:physics",
        "Quantum Physics":"physics:quant-ph",
        "Quantitative Biology":"q-bio",
        "Quantitative Finance":"q-fin",
        "Statistics":"stat"
    }

@app.get("/arx/{name}")
async def arxivscraper(name: str):
    """Retrieve the basic introduction at Arxiv"""
    result = arxiv(name)
    return {"result": result}


"""Search for something you are interested at Arxiv"""
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
