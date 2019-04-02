def count(s):
    l ={}
    l = {char: ord(char) for char in s }
    print (l)
    return l
s = input("Enter a string to analayse")
result = count(s)
print (result)
    
