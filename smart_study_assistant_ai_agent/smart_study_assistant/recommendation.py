import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "sample_data.csv"

def get_recommendations(user_id, course_id):
    # Load sample data
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return ["No data available for recommendations."]
    
    # Filter user and course
    user_data = df[(df['user_id'] == user_id) & (df['course_id'] == course_id)]
    if user_data.empty:
        return ["No records found for this user and course."]
    
    # Identify weak chapters (score < 80)
    weak_chapters = user_data[user_data['score'] < 80]['chapter'].tolist()
    recommendations = []
    if weak_chapters:
        for ch in weak_chapters:
            recommendations.append(f"Review {ch} - your score was below 80.")
    else:
        recommendations.append("Great job! Keep practicing regularly.")
    
    recommendations.append("Try completing the latest practice quiz.")
    recommendations.append("Watch supplementary videos for better understanding.")
    return recommendations

