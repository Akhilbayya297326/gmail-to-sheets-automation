import sys
import os

# Fix path to ensure we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gmail_service import get_gmail_service, fetch_unread_emails
from src.sheets_service import get_sheets_service, append_to_sheet
from src.email_parser import parse_email

def main():
    print("--- Gmail to Sheets Automation ---")
    
    # 1. Authenticate Services
    try:
        gmail = get_gmail_service()
        sheets = get_sheets_service()
    except Exception as e:
        print(f"Error logging in: {e}")
        return

    # 2. Fetch Unread Emails
    messages = fetch_unread_emails(gmail)
    print(f"Found {len(messages)} unread emails.")

    if not messages:
        print("No new emails to process.")
        return

    new_rows = []
    for msg in messages:
        try:
            # 3. Parse Email
            row = parse_email(gmail, msg['id'])
            new_rows.append(row)
            
            # 4. Mark as Read (PREVENTS DUPLICATES)
            # This satisfies the requirement to append only new emails [cite: 25]
            gmail.users().messages().modify(
                userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}
            ).execute()
            print(f"Processed: {row[1]}") # Print subject
            
        except Exception as e:
            print(f"Error processing message {msg['id']}: {e}")

    # 5. Append to Google Sheets
    if new_rows:
        append_to_sheet(sheets, new_rows)
        print("Successfully updated Google Sheet.")

if __name__ == '__main__':
    main()