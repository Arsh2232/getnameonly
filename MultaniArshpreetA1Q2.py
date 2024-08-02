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
