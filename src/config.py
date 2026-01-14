# src/config.py

# Your Spreadsheet ID
SPREADSHEET_ID = '1E-k9hT9cyRyMQRwgbpVrYiJTaxU1UVGL_bqdGj3MsX0' 

# The range to write data to. We start at Sheet1, cell A1
RANGE_NAME = 'Sheet1!A1'

# Scopes required for Gmail and Sheets (Read/Write access)
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/spreadsheets'
]