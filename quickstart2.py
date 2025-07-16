import os.path

from pdfminer.high_level import extract_text
import pikepdf

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
#MAYBE
# from flask import Flask, jsonify, render_template, request
from os import listdir, getenv
from os.path import isfile, join

load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

class Payslips:
    def __init__(self):
        pass
        # self.server = server
        # self.msg_id = msg_id
        # self.attach_id = attach_id
        # self.filename = filename
#main, get_attach, get_pdf, get_msg_id
    def gen_server(self): #SELF?
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
        self.service = service
        return service

    def get_msg_id(self): #SELF?
        """Shows basic usage of the Gmail API.
        Lists ids in Payslips.
        """
        service = self.service
        try:
            # Get list of message IDs
            results = service.users().messages().list(userId='me', labelIds=[os.getenv('PAYSLIPS')], maxResults=55).execute()
            messages = results.get('messages', [])
            # List of all msg ids
            ids = [new_id['id'] for new_id in messages]
            self.ids = ids
            return ids
        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            return f"An error occurred: {error}"

    def get_all_payslips_data(self):#SELF?
        """Scan through gmail Payslips, get data from emails with attachments
        In the format of {filename:{msg_id:attachment_id}}.
        saves as self.all_payslips_data
        """
        service = self.service
        all_payslips_data = {}

        try:
            for msgid in self.ids:  #for all items in list of ids
                #check if have PDF
                message = service.users().messages().get(userId='me', id=msgid).execute()
                for part in message['payload']['parts']:
                    newvar = part['body']
                    if 'attachmentId' in newvar: #if email has attachment
                        filename = part['filename'] #name of file
                        att_id = newvar['attachmentId'] #id of attachment (PDF)

                        file_msg_att = {filename: {msgid:att_id}}#{filename:{msg_id:attachment_id}}
                        all_payslips_data.update(file_msg_att)
            self.all_payslips_data = all_payslips_data
        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            return f"An error occurred: {error}"
        

    def get_pdf(self, filename, msg_id, att_id):#SELF?
        service = self.service


        att = service.users().messages().attachments().get(userId='me', messageId=msg_id, id=att_id).execute()
        data = att['data']
        file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))

        path = os.path.join("payslips", filename) #store_dir,
        f = open(path, 'wb')
        f.write(file_data)
        f.close()
    def check_folder(self):
        """checks Payslips folder and adds files to a list"""
        files = [f for f in listdir("payslips") if isfile(join("payslips", f))]
        return files
    def check_downloadable_files(self, files):
        """Compares self payslips data and filenames in folder
        if files from all_payslips_data are not in folder
        adds them"""
        files_i_dont_have = []
        s = set(files)
        for x in self.all_payslips_data:
            if x not in s:
                files_i_dont_have.append(x)
                s.add(x)
        return files_i_dont_have
    def grab_all_files(self, folder):
        files = [f for f in listdir(folder) if isfile(join(folder, f))]
        return files
    def open_file(self, payslip):
        """takes payslip string
        unlocks pdf if needed  using PDF_PASSWORD in .env
        opens and extracts text"""
        try:
            print(f"📄 Trying to open: {payslip}")
            with open(payslip, 'rb') as f:
                text = extract_text(f)
                if not text:
                    print(f"⚠️ No text found in {payslip}")
                    return None
                return text.split()
        except Exception as e:
            print(f"🔐 Failed to open {payslip} normally: {e}")
            try:
                # Attempt to unlock PDF using password and PikePDF
                pdf = pikepdf.open(payslip, allow_overwriting_input=True, password=os.getenv('PDF_PASSWORD'))
                pdf.save(payslip)
                text = extract_text(payslip)
                if not text:
                    print(f"⚠️ Still no text after unlocking {payslip}")
                    return None
                print(f"🔓 Successfully unlocked and read: {payslip}")
                return text.split()
            except Exception as unlock_error:
                print(f"❌ Could not unlock {payslip}: {unlock_error}")
                return None


# Payslips.get_msg_id()
# print(Payslips.msg_id)

# p = Payslips()       # Create an instance
# p.gen_server()
# p.get_msg_id()  # Call the method on the instance
# p.get_all_payslips_data()

# files = p.check_folder()


# for filename in p.check_downloadable_files(files):
#     filename_dict = p.all_payslips_data[filename]
#     for msg_id, att_id in filename_dict.items():
#         p.get_pdf(filename, msg_id, att_id)

# #--------------------------------------------------------------------------------
# print(p.service) # Access the msg_id attribute of that instance
# print("all payslips data filename:msg_id:attachment_id")
# print(p.all_payslips_data) #filenames

# print("dicks2")
# for _  in p.all_payslips_data["11161601_20230128_EMAIL.pdf"]: #msg_id
#     print(_) #msg_id
#     print(p.all_payslips_data["11161601_20230128_EMAIL.pdf"][_]) #attachment_id
# #--------------------------------------------------------------------------------



#NOTE MAYBE JSONIFY IN THE FUTURE FOR API?