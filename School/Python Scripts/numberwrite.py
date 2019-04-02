#without using inflect
num = int(input("Please enter a number: "))
if num == 1:
    print("one")
if num == 2:
    print("two")
if num == 3:
    print("three")
if num == 4:
    print("four")
if num == 5:
    print("five five")
if num == 6:
    print("six six")
if num == 7:
    print("seven seven")
if num == 8:
    print("eight eight")
if num == 9:
    print("nine nine")
if num == 10:
    print("ten ten")
#With inflect
"""import inflect
num = int(input("Please enter a number: "))
p = inflect.engine()
if num < 5:
    print (p.number_to_words(num))
if num >= 5:
    print (p.number_to_words(num), p.number_to_words(num))""""
