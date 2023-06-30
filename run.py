import gspread 
from google.oauth2.sevice_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorise(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwhiches")

SALES = SHEET.worksheet("sales")

data = sales.get_all_values()
print(data)