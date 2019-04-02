def nameReverse():
    name = raw_input("What is your name: ")
    fName = name.split()[0]
    lName = name.split()[1]
    print lName + ",", fName
    return
choice = input("Which part of the lab do you want? ")
def companyName():
    num = input("How many domains do you want to split: ")
    while num > 0:
        domain = raw_input("Input a domain url: ")
        domain.split('.')
        a, b, c = domain.split('.')
        print b
        num = num -1
def gradeToLetter():
    tries = 0
    while tries != 3:
        grade = input("What is your grade? ")
        if grade >= 97:
            print "A+"
            tries = tries + 1
        elif grade >= 93:
            print "A"
            tries = tries + 1
        elif grade >= 90:
            print "A-"
            tries = tries + 1
        elif grade >= 87:
            print "B+"
            tries = tries + 1
        elif grade >= 83:
            print "B"
            tries = tries + 1
        elif grade >= 80:
            print "B-"
            tries = tries + 1
        elif grade >= 77:
            print "C+"
            tries = tries + 1
        elif grade >= 73:
            print "C"
            tries = tries + 1
        elif grade >= 70:
            print "C-"
            tries = tries + 1
        elif grade >= 67:
            print "D+"
            tries = tries + 1
        elif grade >= 63:
            print "D"
            tries = tries + 1
        elif grade >= 60:
            print "D-"
            tries = tries + 1
        else:
            print "F"
            tries = tries + 1
def wordCount():
    sent = 0
    while sent != 3:
        sen = raw_input("Enter your sentence: ")
        word = sen.split()
        print len(word)
        sent = sent + 1
def wordAverage():
    sen = raw_input("Enter your sentence: ")
    word = sen.split()
    length = len(word)
    
if choice == 1:
    nameReverse()
if choice == 2:
    companyName()
if choice == 3:
    gradeToLetter()
if choice == 4:
    wordCount()
if choice == 5:
    wordAverage()
