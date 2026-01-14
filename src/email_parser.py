import base64
from bs4 import BeautifulSoup

def clean_body(data):
    """Decodes base64 body and converts HTML to plain text."""
    try:
        if not data: return ""
        # Decode the base64 data from Gmail
        decoded_bytes = base64.urlsafe_b64decode(data)
        decoded_str = decoded_bytes.decode('utf-8')
        
        # Strip HTML tags to get plain text (Assignment Requirement)
        soup = BeautifulSoup(decoded_str, "html.parser")
        return soup.get_text(separator=' ').strip()
    except Exception:
        return "(Error parsing body)"

def parse_email(service, msg_id):
    """Extracts From, Subject, Date, and Content."""
    # Get the full email details
    msg = service.users().messages().get(userId='me', id=msg_id).execute()
    payload = msg.get('payload', {})
    headers = payload.get('headers', [])

    # Extract Header Fields
    sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown")
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
    date = next((h['value'] for h in headers if h['name'] == 'Date'), "Unknown")

    # Extract Body (Check if it's plain text or multipart)
    body_data = ""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                body_data = part['body'].get('data', '')
                break
    else:
        # Fallback for simple emails
        body_data = payload.get('body', {}).get('data', '')

    return [sender, subject, date, clean_body(body_data)]