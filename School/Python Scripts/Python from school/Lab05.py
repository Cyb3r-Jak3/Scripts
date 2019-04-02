count = 0
global count
def nameReverse():
    name = raw_input("What is your name: ")
    fName = name.split()[0]
    lName = name.split()[1]
    print lName + ",", fName
    return
choice = input("Which part of the lab do you want? ")
def companyName():
    while count < 3:
        global count
        domain = raw_input("Input a domain url: ")
        domain.split('.')
        a, b, c = domain.split('.')
        print b
        count = count -1
def gradeToLetter():
    global count
    count = 0
    while count < 3:
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
    global count
    while count < 3:
        sen = raw_input("Enter your sentence: ")
        word = sen.split()
        print len(word)
        count = count + 1
def wordAverage():
    global count
    while count < 3:
        sen = raw_input("Enter your sentence: ")
        words = sen.split()
        average = sum(float(len(word)) for word in words)/len(words)
        average = format(average, '.3f')
        print average
        count = count + 1
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
