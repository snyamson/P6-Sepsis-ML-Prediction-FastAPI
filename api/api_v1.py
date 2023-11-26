from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd


# Instance of API Router
router = APIRouter()


# Import the preprocessor and the model
model = joblib.load("./data/models/rf_model.joblib")
preprocessor = joblib.load("./data/models/preprocessor.joblib")


# Create the model for the input data
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


# Create the model for the prediction response
class Prediction(BaseModel):
    ID: str
    Sepsis: str


@router.post("/predict", response_model=Prediction)
async def predict(data: Data) -> Prediction:
    # Column Names
    column_names = ["ID", "PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age"]

    # Convert data to dictionary and then DataFrame
    data_dict = data.model_dump()
    data_df = pd.DataFrame([data_dict], columns=column_names)

    # Save patient ID
    patient_ID = data.ID

    # Drop the ID
    data_df.drop("ID", axis=1, inplace=True)

    # Preprocess the data
    preprocessed_data = preprocessor.transform(data_df)

    # Make a prediction
    prediction = model.predict(preprocessed_data)

    # Format Prediction
    sepsis = "Positive" if str(prediction.item()) == "1" else "Negative"

    # Return prediction
    prediction_instance = Prediction(ID=patient_ID, Sepsis=sepsis)
    return prediction_instance
