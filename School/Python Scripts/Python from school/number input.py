numbers = []
while len(numbers) <= 5:
    numbers.append(input("Input a number: "))
numbers.sort()
if numbers[0] < 5:
    print numbers[0], "Oh my! That is a very small number!"
if numbers[5] > 50:
    print numbers[5], "Whoa! That is a really big number!"
