import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Connect to sheets api

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("testsheets.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("contain_names").sheet1
data = sheet.get_all_records()
collum = sheet.col_values(1)
logins = sheet.col_values(3)
age_user = sheet.col_values(2)

#Login username prompt

def user():
 name = input("Please type in a username: ")
 if name in collum:
       print("OK")
 else:
       quit()

def password():
  creds = input("Please type in a password: ")
  if creds in logins:
        print("OK")
  else:
        print("Invalid password")
        quit()

def age():
  godini = input("Please Confirm you're +18: yes/no ")
  if godini in age_user:
        print("OK")
  else:
        print("Invalid, you're not eligible for joining.")

#Call functions

user()
password()
age()