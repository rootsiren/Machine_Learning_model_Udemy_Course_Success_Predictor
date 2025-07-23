from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://machine-learning-model-udemy-course-success-predictor-nqp94qbb.streamlit.app/"],  # replace "*" with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected request body model
class DataModel(BaseModel):
    data: str

@app.post("/api/endpoint")
async def receive_data(payload: DataModel):
    # Just echo back the received data
    return {"received": payload.data}
