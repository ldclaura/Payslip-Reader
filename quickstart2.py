import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#env files
import os
from dotenv import load_dotenv
#base64
import base64


load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

class Payslips:
    def __init__(self, server, msg_id, attach_id, filename):
        self.server = server
        self.msg_id = msg_id
        self.attach_id = attach_id
        self.filename = filename
#main, get_attach, get_pdf, get_msg_id
    def main(): #SELF?
        """Shows basic usage of the Gmail API.
        Generate the Server
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(os.getenv('TOKEN')):
            creds = Credentials.from_authorized_user_file(os.getenv('TOKEN'), SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.getenv('TOKEN'), SCOPES
                )
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(os.getenv('TOKEN'), "w") as token:
                token.write(creds.to_json())
        # Connect to Gmail API
        service = build('gmail', 'v1', credentials=creds)
        return service
    def get_msg_id(): #SELF?
        pass
    def get_attach_id():#SELF?
        pass
    def get_filename():#SELF?
        pass
    def get_pdf():#SELF?
        pass