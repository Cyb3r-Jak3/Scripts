def program():
    Error = False
    completed = False
    while not Error and not completed:
        user = input("Input a number: ")
        numDigit = 0
        if user <= 0:
            Error = True
        while user > 0:
            user = user / 10
            numDigit += 1
            completed = True

    if completed == True:
        print"There are", str(numDigit), "digits in the number: ", user, "\n"
        completed = False
        print"Enter a zero or negitive number to exit \n"
        program()
program()
