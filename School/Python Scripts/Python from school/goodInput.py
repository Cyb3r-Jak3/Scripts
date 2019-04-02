def program():
    working = True
    nums = [1,2,3,4,5,6,7,8,9,10]
    while working:
        user = input("Please input a number between 1-10 \n")
        if user in nums:
            working = False
        elif user > 10:
            print("That number is too high")
        elif user < 1:
            print("That number is too low")
        else:
            print("That is not valid input")
    print"Correct", user, "was a valid entry"
program()
