from fastapi import FastAPI
from models import UserProfile
from workout_engine import generate_program_parameters
from llm_generator import generate_workout_plan
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/generate-workout")
def create_workout(profile: UserProfile):

    parameters = generate_program_parameters(profile)

    workout_plan = generate_workout_plan(profile, parameters)

    return workout_plan