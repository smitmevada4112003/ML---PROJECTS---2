from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

model = pickle.load(open("salse_prediction1.pkl", "rb"))

print(model.predict([[4,1122.63,466]]))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "all okk and done"}

@app.post("/predict")
def predict(data: dict):

    category = int(data["category"])
    price = int(data["price"])
    stock = int(data["stock"])

    result = model.predict([[category, price, stock]])

    return {
        "category": category,
        "price": price,
        "stock": stock,
        "prediction": int(result[0])
    }