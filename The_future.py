import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Connect to sheets api
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("testsheets.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("contain_names").sheet1
data = sheet.get_all_records()
collum = sheet.col_values(1)
parola = sheet.col_values(3)
vuzrast = sheet.col_values(2)
#print(collum) tva samo za da vidq dali google durpa data. inache ne e nujno da displayva


#Login username prompt
# ask for user input, if name in sheets + creds in sheet are found print Salute. Else print Invalid
def user():
 name = input("Please type in a username: ")
 if name in collum:
       print("OK")
 else:
       quit()
def password():
  creds = input("Please type in a password: ")
  if creds in parola:
        print("OK")
  else:
        print("Invalid")
def age():
  godini = input("Please Confirm you're +18: yes/no ")
  if godini in vuzrast:
        print("OK")
  else:
        print("Invalid")


user()
password()
age()




