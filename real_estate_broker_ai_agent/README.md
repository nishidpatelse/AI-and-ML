# 🏡 Real Estate Broker AI

This is a Python-based AI-powered virtual real estate broker built using FastAPI, spaCy, and Google Calendar API. It can understand user requirements in natural language, match suitable properties, and schedule meetings with human agents.

---

## 🚀 Features

### ✅ 1. Natural Language Understanding
- Accepts free-form user queries like:
  > "Looking for a 2BHK apartment in New York between $3000 to $5000 with gym and parking, and pet-friendly."
- Uses spaCy to extract structured requirements:
  - **Location**
  - **Budget (min/max)**
  - **Property Type** (apartment, villa, etc.)
  - **Size & BHK**
  - **Facilities** (pool, gym, parking, etc.)
  - **Pet-friendliness**

### 🏘️ 2. Property Matching
- Loads sample listings from a JSON file.
- Filters listings based on the extracted requirements.

### 📅 3. Meeting Scheduling
- Integrates with Google Calendar.
- Lets users schedule appointments with human agents.
- Sends Google Calendar invites.

### 💾 4. SQLite Logging (Optional)
- Logs all user queries to a local database (`interactions.db`) for audit or analytics.

---

## 📂 Project Structure

```
real_estate_broker_ai/
├── app/
│   ├── main.py                # FastAPI app
│   ├── models.py              # Pydantic models (optional)
│   ├── sample_data/listings.json
│   └── utils/
│       ├── nlp_parser.py      # NLP-based requirement extraction
│       ├── property_matcher.py# Property filtering
│       ├── calendar_api.py    # Google Calendar integration
│       └── db.py              # Interaction logger
├── .env                       # Contains API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone <repo-url>
cd real_estate_broker_ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 3. Setup `.env`

Create a `.env` file with:

```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/oauth2callback
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

### 5. Access the API

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## 📬 API Endpoints

- `POST /search`: Extracts requirements from user input and returns matching listings.
- `POST /schedule`: Triggers Google Calendar meeting creation.

---

## 🔒 Security Notes

- Do not commit `.env` or `credentials.json`.
- Use HTTPS in production.
- Ensure Google Calendar OAuth credentials are secured.

---

## 📈 Future Improvements

- Add authentication & user sessions
- Connect to a real listings API (e.g., Zillow)
- Improve NLP accuracy using GPT models or fine-tuned transformers
- Add a React/Vue frontend

---

Made with ❤️ for smarter real estate interactions.
