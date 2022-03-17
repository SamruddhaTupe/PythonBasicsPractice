def listrev(thelist):
    astring = ''.join(thelist) #Converting the list into a string.
    alist = astring.split(' ') #Converting the string into a list but with words as elements as opposed to letters as elements.
    thefinallist = [] #A list that is used in the for loop to interchange the words as per the request.
    #For loop to interchange the words.
    for i in range(0, len(alist)):
        thefinallist.append(alist[len(alist)-i-1])
        if i != (len(alist)-1):
            thefinallist.append(' ')
    #Converting the list into a string.
    finalstring = ''.join(thefinallist)
    #Converting the string into a list but with characters as elements.
    return list(finalstring.strip(" "))
alist = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
print(listrev(alist))
