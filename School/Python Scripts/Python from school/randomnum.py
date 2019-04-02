from random import randint
randomNum = randint(0,9)
usernum = input("Enter your guess: ")
if usernum == randomNum:
    print "Correct"
else:
    print "The number was", str(randomNum), "and you guessed", str(usernum) + ". Better luck next time"
