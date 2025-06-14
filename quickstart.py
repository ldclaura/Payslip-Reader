import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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
    unread_msgs = service.users().messages().list(userId='me',labelIds=["INBOX"]).execute()
    mssg_list = unread_msgs['messages']
    print ("Total unread messages in inbox: ", str(len(mssg_list)))

    final_list = [ ]

    for mssg in mssg_list:
      temp_dict = { }
      m_id = mssg['id'] # get id of individual message
      message = service.users().messages().get(userId='me', id=m_id).execute() # fetch the message using API
      payld = message['payload'] # get payload of the message 
      headr = payld['headers'] # get header of the payload
      for _ in headr:
        if _['name'] == 'From':
          if _['value'] == "": #work from email
            print(_['value'])


  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()
