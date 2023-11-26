from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


# Create the structure of the data
class Data(BaseModel):
    ID: str
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: int


# Create the structure of the response prediction
class Prediction(BaseModel):
    ID: str
    Sepsis: str


@router.post("/predict", response_model=Prediction)
async def predict(data: Data) -> Prediction:
    predicted = Prediction(ID="", Sepsis="Sepsis Prediction")
    return predicted
