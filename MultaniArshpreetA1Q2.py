###MultaniArshpreetA1Q2


#COMP 1012 SECTION A01
#INSTRUCTOR [Phil]
#ASSIGNMENT: A1 Question 2
#AUTHOR [Arshpreet Multani]
#VERSION [07-05-24]
#PURPOSE: initialize a variable and perform four operations 
###
#question 2
#asking user for input and using lower() to convert to small letters even if the user types in capital letters
userURL = input("Please enter your URL ").lower()
print(userURL)
#using .strip() with argument .www to remove it 
print("Removing www.")
noWWW= userURL.strip("www.")
print(noWWW)
#using .strip() to remove .com
print("Removing .com")
finalString=noWWW.strip(".com")
print(finalString)