from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_service():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)
    return service

def schedule_meeting(service, email, summary="Real Estate Inquiry"):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    event = {
        'summary': summary,
        'start': {'dateTime': '2025-05-15T10:00:00-07:00', 'timeZone': 'America/Los_Angeles'},
        'end': {'dateTime': '2025-05-15T10:30:00-07:00', 'timeZone': 'America/Los_Angeles'},
        'attendees': [{'email': email}],
    }
    return service.events().insert(calendarId='primary', body=event).execute()
