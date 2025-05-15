# Smart Study Assistant for LMS

## Overview

Smart Study Assistant is an AI-powered agent designed to integrate with a Learning Management System (LMS). It enhances the learning experience by providing personalized study content, micro-learning tips, and answering course-related questions.

## Features

- **Personalized Recommendations**: Based on student performance and learning history.
- **Micro-Learning Prompts**: Short quizzes and tips to reinforce learning.
- **Q&A Agent**: NLP-powered agent to answer student queries from course materials.
- **Study Habit Tracker**: Monitors learning behavior and provides feedback.


## Setup

1. Clone this repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run the main application:
  ```bash
  python smart_study_assistant/main.py
  ```

# Smart Study Assistant

This AI agent offers:
- Natural language Q&A
- Study habit tracking
- Personalized recommendations
- REST API for LMS integration

## Run the API server

```bash
pip install fastapi uvicorn pandas pydantic
uvicorn smart_study_assistant.api:app --reload
```

## Dependencies

- Python 3.8+
- OpenAI / HuggingFace Transformers
- FastAPI / Flask (optional frontend/backend)
- PyYAML


## Streamlit UI

To launch the Streamlit UI:

```bash
streamlit run smart_study_assistant/streamlit_app.py
```

This will open a browser-based interface for interacting with the study assistant.
