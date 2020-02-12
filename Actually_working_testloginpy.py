import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Connect to sheets api
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("testsheets.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("contain_names").sheet1
data = sheet.get_all_records()
collum = sheet.col_values(1)
#print(collum) tva samo za da vidq dali google durpa data. inache ne e nujno da displayva
#vuprosnata data predi user input prompta
parola = sheet.col_values(3)
#print(parola)

#Login username prompt
def user():
 name = input("Pleas type in a username: ")

 if name in collum:
     print("Salute, " + name)

 else:
     print("Invalid")

user()

def login():
    creds = input("Please type in a password: ")
    if creds in parola:
        print("OK")
    else:
        print("Invalid")

login()