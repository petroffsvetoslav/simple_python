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

#Login prompt
def user():
 name = input("User input: ")

 if name in collum:
    print("Salute")
    input("Please type in a password: ")

 #elif name == "sam": tva tuka e ako tursq konkreten user i samo toi trqbva da ima access.
    # Trqbva gornoto da e if name == "Sam" + toq red koito e lowercase sam da dava wrong
    #print("Wrong")
 else:
     print("Invalid")

user()