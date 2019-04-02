def program():
    fin = False
    while not fin:
        numList = [1,3,5,7,9,11,13,15,17,19]
        user = input("Enter a number to find: ")
        try:
            found = numList.index(user) + 1
            fin = True
        except ValueError:
            print "Number:", user, "not in list"
        if fin:
            print"Number:", user, 'was in the number', found, " spot in the list \n"
            fin = False
    
program()
