from recommendation import get_recommendations
from qa_agent import answer_question
from habit_tracker import track_study_habits

def main():
    print("Smart Study Assistant")
    
    user_id = "student123"
    course_id = "math101"

    print("\n--- Recommendations ---")
    recommendations = get_recommendations(user_id, course_id)
    for rec in recommendations:
        print(f"- {rec}")

    print("\n--- Ask a Question ---")
    question = "What is the Pythagorean theorem?"
    print(f"Q: {question}")
    print("A:", answer_question(question))

    print("\n--- Study Habit Tracker ---")
    habits = track_study_habits(user_id)
    print(habits)

if __name__ == "__main__":
    main()
