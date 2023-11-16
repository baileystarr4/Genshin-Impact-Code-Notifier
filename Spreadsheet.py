import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Spreadsheet:
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    CODE_SPREADSHEET_ID  = "1PSw3drnP-2jTlfbcF54P_xqZb937-6nXjoo6VRZt5pw"
    USER_DATA_SPREADSHEET_ID = "17buirFEEmgc8DctZV4XvIUaIK2JfUH_hbPgy0W0s40s"

    def __init__(self):
        self.creds = None

        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
                token.write(self.creds.to_json())
    
    def read_code_spreadsheet(self):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=self.CODE_SPREADSHEET_ID, range="Sheet1")
                .execute()
            )
            values = result.get("values", [])

            
            return values

        except HttpError as err:
            print(err)

    def read_user_data_spreadsheet(self):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=self.USER_DATA_SPREADSHEET_ID, range="Sheet1")
                .execute()
            )
            values = result.get("values", [])

            return values

        except HttpError as err:
            print(err)
            
    def write_to_code_spreadsheet(self, link):
        try:
            service = build("sheets", "v4", credentials=self.creds)
            sheet = service.spreadsheets()
            sheet.values().append(spreadsheetId=self.CODE_SPREADSHEET_ID, range="Sheet1", valueInputOption="USER_ENTERED", body={"values": [[f"{link}"]]}).execute()

        except HttpError as err:
            print(err)

    def write_to_user_data_spreadsheet(self, user_data_list):
        try:
            service = build("sheets", "v4", credentials=self.creds)
            sheet = service.spreadsheets()
            sheet.values().append(spreadsheetId=self.USER_DATA_SPREADSHEET_ID, range="Sheet1", valueInputOption="USER_ENTERED", body={"values": [user_data_list]}).execute()

        except HttpError as err:
            print(err)

    def find_user(self, phone_number):
        data = self.read_user_data_spreadsheet()
        user_row = -1
        for i in range(len(data)):
            if i == 0:
                continue
            if phone_number in data[i]:
                user_row = i
                break
        return user_row
    
    def delete_user(self, user_row):
        request_body = {
            "requests" :[
                {
                "deleteDimension": {
                    "range": {
                        "sheetId": 0,
                        "dimension": "ROWS",
                        "startIndex": user_row,
                        "endIndex": user_row + 1
        }}}]}              
        
        service = build("sheets", "v4", credentials=self.creds)
        sheet = service.spreadsheets()
        deleting = sheet.batchUpdate(spreadsheetId=self.USER_DATA_SPREADSHEET_ID, body=request_body)
        deleting.execute()