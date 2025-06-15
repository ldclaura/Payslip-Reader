import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#env files
import os
from dotenv import load_dotenv

load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
      print("No labels found.")
      return
    print("Labels:")
    for label in labels:
      print(label["name"])
      for label in results['labels']:
        print(f"{label['name']} — {label['id']}")

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

def main2():
  """Shows basic usage of the Gmail API.
  Lists From and Subject.
  """
  creds = None

  # Load saved credentials
  if creds is None and os.path.exists('token.json'):
      creds = Credentials.from_authorized_user_file('token.json', SCOPES)

  # If no valid creds, prompt login
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save credentials
      with open('token.json', 'w') as token:
          token.write(creds.to_json())

  # Connect to Gmail API
  service = build('gmail', 'v1', credentials=creds)

  # Get list of message IDs
  results = service.users().messages().list(userId='me', labelIds=[os.getenv('PAYSLIPS')], maxResults=10).execute()
  messages = results.get('messages', [])

  # Print message subjects and senders
  for msg in messages:
      msg_id = msg['id']
      msg_data = service.users().messages().get(userId='me', id=msg_id, format='metadata', metadataHeaders=['Subject', 'From']).execute()
      headers = msg_data['payload']['headers']
      subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
      sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
      print(f"From: {sender}\nSubject: {subject}\n")
      if sender == os.getenv('WORK_SENDER'):
        print("yes")
        





if __name__ == "__main__":
  main()
  main2()