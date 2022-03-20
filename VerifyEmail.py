import re
email = input("Enter email to be verified:\n\n")
if re.search("\s", email):
    print(email + " is not valid number as white space is there.\n")
else:
    verify = re.search("^[a-z0-9_]+[a-z0-9\.-_]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email)
    print(email + " is a valid email.\n") if verify else print("The email is not a valid email if")
