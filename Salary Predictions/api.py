from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

# uvicorn api:app reload

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
model = joblib.load(r"C:\Users\SMIT\OneDrive\Desktop\SalaryPredictions\API1.joblib")


@app.get("/")
def home():
    return {"message": "All Ok"}


@app.post("/predict")
def predict(data: dict):

    years = data["YearsExperience"]

    result = model.predict([[years]])

    return {
        "YearsExperience": years,
        "PredictedSalary": float(result[0])
    }