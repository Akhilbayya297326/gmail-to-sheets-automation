import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from src.config import SCOPES

def get_gmail_service():
    """Authenticates and returns the Gmail service."""
    creds = None
    # Check if token.json exists (stores your login session)
    if os.path.exists('credentials/token.json'):
        creds = Credentials.from_authorized_user_file('credentials/token.json', SCOPES)
    
    # If no valid credentials, log in via browser
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Load your credentials.json file
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the new session to token.json
        with open('credentials/token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def fetch_unread_emails(service):
    """Fetches unread emails from the Inbox."""
    # This query 'is:unread label:INBOX' satisfies the requirement to read unread emails
    results = service.users().messages().list(userId='me', q='is:unread label:INBOX').execute()
    return results.get('messages', [])