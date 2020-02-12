#import modues (like math) at the top of the code to use everywhere
from math   import *
print(floor(3.2))

# set variables containing strings, always must be in " "
name = "Svetoslav"
age = "21"
is_male = True


#print string and use + to include variable
print("There was a young guy named " + name)
print("he enjoyed studying about computers.")
print("Before he was " + age +", he didn't know about this passion")
print("just used the PC to play games and stuff")
print("He liked geometry")

#Use \n to move something one line down
print("   /|")
print("  / |")
print(" /  |")
print("/_ _|")
print(" ___")
print("|   |")
print("|   |")
print("|   | \n|___|")

#Use \ to litelery otuput something
print("He is \"not human\".")
phrase = "Strive to improve,\nAlways."
signed = "since \"1993\""
person = "Svetoslav"

#Use + to add variable and another variable on the same lie
print(phrase + signed   + "\nSvetoslav")
print(person)

#Functions = variable + . and TAB and functions always have () after their option
love = "family, Maggy"
print(love.upper())
#Shows if the string inside the variable is all upper case/ either True or False
print(love.isupper())
#To combine functions end first one with () and use . to define the next which will also end with ()
print(love.upper().isupper())
#Use [] to print particular character - numbering start @ 0
print(love[8])

print(love.replace("family", "Family").isupper())
#Show the number of a character inside the string
print(love.index("M"))
# use .replace function to replace strings and input the existing first, followed by a , to add the new thing
print(love.replace("Maggy","Bebinka"))

#strings must always be in "", numbers don't
print(2)
print("forearm")
print(3+7.25)
print(-25 * (2+3))
number = 9
print(number + 5)
print(number + 5 * (18-1))
#Convert numbers to strings using str(variable_name) to use them with strings
print(str(number) + " favourite")

#Common functions to use with numbers - abs, pow, max/min
number = -8
#print the absolute value with abs function
print(abs(number))
print(max(2, -6)) #prints the bigger of the provided numbers
print(floor(3.7))

# User Input
input("Type in your name: ")
#Storing user input in a variable for later use
user_name = input("Verify your name please: ")
print("Hello " + user_name + "!")
user_age = input("Please type in your age: ")
print(user_age)
print(user_name   +   " ,You are "   +   user_age)

#Lists
friends = ["Maggy", "Lary", "Samuel Jackson"]
print(friends)
# you can print particular parts of your list via indexing
print(friends[0])
print(friends[1])
# you can reindex things e.g. -
friends[1] = "Zahari" #this changes list one index 1 from Lary to Zahary
print(friends[1])
#this prints indexes FROM - TO without including the actual ending index
print(friends[0:2])
#reverse index using (count indexes from right -> left starting with -1 not 0 as usually.
print(friends[-2])

#List functions

lucky_numbers = [1, 7, 9, 17, 22]
friends = ["Maggy", "Lari", "Molly", "Samuel Jackson"]
print(friends)

#To add more entries to existing list use append ALWAYS ADDS ENTRY AT THE END OF THE LIST
friends.append("Nov fr")
print(friends)

#Add entries somewhere you actually want in the list
friends.insert(3, "Na Samuel Brat mu")
print(friends)

#Remove some list entry you want via index
friends.remove("Na Samuel Brat mu")
print(friends)

#Combine the two list (da se addne ediniq v kraq na drugiq) LIST.EXTEND
friends.extend(lucky_numbers)
print(friends)

#Get the index of an entry in the list (ONLY WORKS WITH STRINGS AS FAR AS I KNOW FOR NOW)
print(friends.index('Maggy'))
print(friends)

#Tuples are container like and can store information (like lists) but are unmuttable (they can't be changed once the value is set)
coordinates = (4, 5)
print(coordinates[1])

#Create list of coordinates CHOOSE TO USE TUPLES WHEN YOU WANT TO STORE DATA THAT CANNOT BE MODIFIED
coordinates_two = [(2, 80), (33, 28), (4,5)]
print(coordinates_two[1])

#Functions
#Functions use "PARAMETERS"
def greatings():
    print("Hello and welcome")

greatings()

def list_function():
    sample_fam = [1, 3, 8]
    print(sample_fam)

list_function()

greatings()

#giving parameters to a function
def ask_for_name():
    user_ime = input("Please type in a name: ")
    print("Hello "  +   user_ime)
ask_for_name()