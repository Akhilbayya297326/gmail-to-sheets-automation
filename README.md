# Gmail to Google Sheets Automation

**Author:** [Bayya Akhil]
**Date:** January 14, 2026

## Project Overview
This Python automation script connects to the Gmail API to fetch unread emails and logs them into a Google Sheet. It uses OAuth 2.0 for secure authentication and ensures that only new emails are processed.

## Architecture
[User] -> [Gmail API] -> [Python Script] -> [Google Sheets API]
                               |
                        [State Management]
                     (Marks emails as Read)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-repo-link>
   cd gmail-to-sheets

   