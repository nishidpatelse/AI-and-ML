import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "study_sessions.csv"

def track_study_habits(user_id):
    # Study session data: user_id,date,duration_minutes
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return {"error": "No habit data available."}
    
    user_sessions = df[df['user_id'] == user_id]
    if user_sessions.empty:
        return {"error": "No sessions found for this user."}
    
    total_sessions = len(user_sessions)
    avg_duration = user_sessions['duration_minutes'].mean()
    
    # Days studied in last 7 days
    user_sessions['date'] = pd.to_datetime(user_sessions['date'])
    last_week = datetime.now() - timedelta(days=7)
    recent_sessions = user_sessions[user_sessions['date'] >= last_week]
    days_studied = recent_sessions['date'].dt.strftime('%A').unique().tolist()
    
    return {
        "total_sessions": total_sessions,
        "average_duration_min": round(avg_duration, 1),
        "days_studied_last_week": days_studied
    }

