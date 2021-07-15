from fastapi import FastAPI
from model import *
app = FastAPI()

from pydantic import BaseModel


class Item(BaseModel):
    review: str


@app.get("/")
def read_root():
    return {"Message": "API is running"}


@app.post("/api/")
def create_item(item: Item):
    lrmodel,cv=get_model()
    prediction=lrmodel.predict(cv.transform([item.review]))
    return {"Message": 'Positive' if prediction[0] else 'Negative'}