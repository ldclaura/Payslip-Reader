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


def main():
  """Shows basic usage of the Gmail API.
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

def main_copied(serv):
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  service = serv


  try:

    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
      print("No labels found.")
      return
    print("Labels:")
    for label in labels:
      print(label["name"])

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


def list_from_subject(serv):
  """Shows basic usage of the Gmail API.
  Lists From and Subject.
  """

  # Connect to Gmail API
  service = serv
  # Get list of message IDs
  results = service.users().messages().list(userId='me', labelIds=[os.getenv('PAYSLIPS')], maxResults=1).execute()
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
        

def get_attach(serv):
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  service = serv
  try:
    # Get list of message IDs
    results = service.users().messages().list(userId='me', labelIds=[os.getenv('PAYSLIPS')], maxResults=1).execute()
    messages = results.get('messages', [])

    # Print message subjects and senders
    for msg in messages:
        msg_id = msg['id']
        print(msg_id)
    #Get PDF
    message = service.users().messages().get(userId='me', id=msg_id).execute()
    for part in message['payload']['parts']:
      newvar = part['body']
      if 'attachmentId' in newvar:
          att_id = newvar['attachmentId']
          att = service.users().messages().attachments().get(userId='me', messageId=msg_id, id=att_id).execute()
          data = att['data']
          file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
          print(part['filename'])
          filename = part['filename']
          path = os.path.join("payslips", filename) #store_dir,
          f = open(path, 'wb')
          f.write(file_data)
          f.close()





  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

def select_payslips_emails(serv):
  """Shows basic usage of the Gmail API.
  Selects latest 10 emails from payslips.
  """
  try:
    # Call the Gmail API
    service = serv
    # Get list of message IDs
    results = service.users().messages().list(userId='me', labelIds=[os.getenv('PAYSLIPS')], maxResults=1).execute()
    messages = results.get('messages', [])

    # Print message subjects and senders
    for msg in messages:
        msg_id = msg['id']
        print(msg_id)

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  tokengen = main()
  tokengen
  print(main_copied(tokengen))
  list_from_subject(tokengen)
  get_attach(tokengen)




# def GetAttachments(service, user_id, msg_id, store_dir):

# """Get and store attachment from Message with given id.

# Args:
# service: Authorized Gmail API service instance.
# user_id: User's email address. The special value "me"
# can be used to indicate the authenticated user.
# msg_id: ID of Message containing attachment.
# prefix: prefix which is added to the attachment filename on saving
# """
# try:
#     message = service.users().messages().get(userId=user_id, id=msg_id).execute()
#     for part in message['payload']['parts']:
#         newvar = part['body']
#         if 'attachmentId' in newvar:
#             att_id = newvar['attachmentId']
#             att = service.users().messages().attachments().get(userId=user_id, messageId=msg_id, id=att_id).execute()
#             data = att['data']
#             file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
#             print(part['filename'])
#             path = ''.join([store_dir, part['filename']])
#             f = open(path, 'wb')
#             f.write(file_data)
#             f.close()
# except errors.HttpError, error:
#     print 'An error occurred: %s' % error

