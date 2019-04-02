import random, sys
def again():
    again = raw_input("Play again (yes/no) \n")
    if again.lower().startswith('y'):
        program()
    if again.lower().startswith('n'):
        sys.exit

def program():
    secretNumber = random.randrange(0, 100)
    numguess = 0
    while numguess != 7:
        user = input('Enter a number between 0-100 \n')
        if user == secretNumber:
            print"You win in", numguess, "guesses!"
            again()
        elif user > secretNumber:
            print"Your guess was too big"
            numguess += 1
        elif user < secretNumber:
            print"Your guess was too small"
            numguess +=1

    print"Sorry, you lose. The number was", secretNumber
    again()

program()
