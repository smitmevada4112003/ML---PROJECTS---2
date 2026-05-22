from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
with open("Salary_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {
        "message": "Dhrumil Joshimmm"
    }

@app.post("/predict")
def predict(data: dict):

    exp = data.get("YearsExperience")

    if exp is None:
        return {
            "error": "YearsExperience required"
        }

    result = model.predict([[exp]])

    return {
        "YearsExperience": exp,
        "Salary": int(result[0])
    }