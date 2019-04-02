import random
def list_Shuffle():
    listlen = input("How many numbers would you like in your list? ")
    nums = []
    while len(nums) < listlen:
        nums.append(input("Enter a number: "))
    random.shuffle(nums)
    print (nums)
list_Shuffle()
