numbers = []
while len(numbers) <= 5:
    numbers.append(int(input("Input your number: ")))
numbers.sort()
if numbers[0] < 5:
    print ('Woah that number is really small', numbers[0])
if numbers[5] > 50:
    print ('Woah that number is really big', numbers[5])
print (numbers)
