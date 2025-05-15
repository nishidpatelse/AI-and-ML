from smart_study_assistant.qa_agent import answer_question

def test_answer_question():
    assert "pythagorean" in answer_question("What is the Pythagorean theorem?").lower()
