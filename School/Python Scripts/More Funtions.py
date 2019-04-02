def sumN():
    nums = []
    count = input("How many numbers would you like to enter? ")
    while len(nums) < int(count):
         nums.append(input("Enter a Number > "))
    print (sum(nums))

def sumCubes():
    total = 0
    nums = []
    count = input("How many numbers would you like to enter? ")
    while len(nums) < int(count):
         nums.append(input("Enter a Number > "))
    for i in nums:
        total += pow(int(i), 3)
    print(total)

def area():
    width = int(input("What is the width of the rectangle: "))
    height = int(input("What is the height of the reactangle: "))
    area = width * height
    print (area)
    
def square():
    nums = []
    count = input("How many numbers would you like to enter? ")
    while len(nums) < int(count):
         nums.append(input("Enter a Number > "))
    for i in nums:
        print("The sqaure of", i, "is", int(i) * int(i))

funtion = input("Which funtion would you like? \n"
                "sumN --> 1 \n"
                "sumCube --> 2 \n"
                "Area of Rectangle --> 3 \n"
                "sqaureEach --> 4 \n")
if funtion == '1':
    sumN()
if funtion == '2':
    sumCubes()
if funtion == '3':
    area()
if funtion == '4':
    square()
    
