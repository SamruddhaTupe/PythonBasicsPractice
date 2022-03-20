import re
def everify(theaddress):
    if re.search("\s", theaddress):
        return theaddress+" is not valid number as white space is there.\n"
    else:
        verify = re.search("^[a-z0-9_]+[a-z0-9\.-_]?[a-z0-9]+[@]\w+[.]\w{2,3}$", theaddress)
        if verify:
            return " is a valid email.\n"
        else:
            return "The email is not a valid email"
email = input("Enter email to be verified:\n\n")
print(email,everify(email))
