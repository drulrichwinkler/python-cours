"""Solution 05 -- Bounds in the model."""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


class Sample(BaseModel):
    """One submitted reading."""

    tag: str = Field(min_length=4)
    celsius: float = Field(gt=-50, lt=200)
    location: str = "unknown"


app = FastAPI()


@app.post("/sample")
def take(sample: Sample) -> dict[str, str]:
    """Accept a reading and answer with its tag."""
    return {"tag": sample.tag}


client = TestClient(app)

bodies = [
    {"tag": "TH-04", "celsius": 93.5},
    {"tag": "TH", "celsius": 93.5},
    {"tag": "TH-04", "celsius": -99},
    {"celsius": 20},
]

for body in bodies:
    response = client.post("/sample", json=body)
    if response.status_code == 200:
        print(response.status_code, response.json()["tag"])
    else:
        print(response.status_code, response.json()["detail"][0]["type"])
