import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Spreadsheet:
    SCOPES = ["http://googleapis.com/auth/spreadsheets"]
    CODE_SPREADSHEET_ID  = "1PSw3drnP-2jTlfbcF54P_xqZb937-6nXjoo6VRZt5pw"
    USER_DATA_SPREADSHEET_ID = "17buirFEEmgc8DctZV4XvIUaIK2JfUH_hbPgy0W0s40s"

