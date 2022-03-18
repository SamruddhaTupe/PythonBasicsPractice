#Importing Regular Expressions
import re
#Taking an integer input to ensure only digits are there, and then converting the number into a string
number = str(int(input("Enter number to be verified:\n\n")))
#Condition for a valid number. Length must be 10 digits only.
if len(number) == 10:
    #Using regular expressions to check if the string is starting with 7, 8, 9 any of the three digits or not.
    verify = re.search("^[789].*", number)
    #Regular expression 'search' returns an object if match is found, else None is returned
    if verify:
        print(number+" is a valid number.\n")
    elif verify == None:
        print(number+" is not a valid number.\n")
else:
    print(number+" is not a valid number.\n")



