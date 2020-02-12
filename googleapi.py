import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("testsheets.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("contain_names").sheet1
data = sheet.get_all_records()
print(data)