from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import nlp_parser, property_matcher, calendar_api

app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/search")
def search_properties(query: Query):
    requirements = nlp_parser.extract_requirements(query.user_input)
    listings = property_matcher.load_properties()
    matches = property_matcher.match_properties(requirements, listings)
    return {"requirements": requirements, "matches": matches}

@app.post("/schedule")
def schedule_meeting(email: str):
    service = calendar_api.get_service()
    event = calendar_api.schedule_meeting(service, email)
    return {"event": event}
