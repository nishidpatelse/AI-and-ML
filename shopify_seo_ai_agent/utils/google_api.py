
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE')
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def get_search_analytics(site_url, start_date, end_date):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('searchconsole', 'v1', credentials=credentials)
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query']
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
    return response
