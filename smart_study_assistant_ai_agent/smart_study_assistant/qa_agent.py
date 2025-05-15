FAQ = {
    "pythagorean theorem": "The Pythagorean theorem states that in a right triangle, a² + b² = c².",
    "quadratic formula": "The quadratic formula is x = (-b ± √(b²-4ac)) / (2a).",
    "derivative": "A derivative represents the rate of change of a function with respect to a variable."
}

def answer_question(question):
    question_lower = question.lower()
    for key, answer in FAQ.items():
        if key in question_lower:
            return answer
    return "Sorry, I don't have an answer for that. Please ask another question or check your course materials."

