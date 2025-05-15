from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from smart_study_assistant.recommendation import get_recommendations
from smart_study_assistant.qa_agent import answer_question
from smart_study_assistant.habit_tracker import track_study_habits

app = FastAPI(title="Smart Study Assistant API")

class RecommendationRequest(BaseModel):
    user_id: str = Field(..., example="student123")
    course_id: str = Field(..., example="math101")

class RecommendationResponse(BaseModel):
    recommendations: List[str]

class QARequest(BaseModel):
    question: str = Field(..., example="What is the Pythagorean theorem?")

class QAResponse(BaseModel):
    answer: str

class HabitRequest(BaseModel):
    user_id: str = Field(..., example="student123")

class HabitResponse(BaseModel):
    total_sessions: int
    average_duration_min: float
    days_studied_last_week: List[str]

@app.post("/recommendations", response_model=RecommendationResponse)
def recommendations(req: RecommendationRequest):
    recs = get_recommendations(req.user_id, req.course_id)
    if not recs:
        raise HTTPException(status_code=404, detail="No recommendations found.")
    return {"recommendations": recs}

@app.post("/ask", response_model=QAResponse)
def ask(req: QARequest):
    ans = answer_question(req.question)
    return {"answer": ans}

@app.post("/habits", response_model=HabitResponse)
def habits(req: HabitRequest):
    result = track_study_habits(req.user_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
