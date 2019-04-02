#words =  "hello my amazing hello this is a super long string Super long random words are amazing to just keep typing"
words = input("Enter your string\n")

def word_count(string):
    my_string = string.lower().split()
    my_dict = {}
    total = 0
    for item in my_string:
        total += 1
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    return(my_dict, total)

myDict = word_count(words)
total_words = myDict[1]
myDict = myDict[0]
Sorted = sorted(((value,key) for (key,value) in myDict.items()), reverse=True)
total = 0
for x in range(len(Sorted)):
    print(str(Sorted[x][1]).title(),"appears", Sorted[x][0],"times and occurs",  str(((Sorted[x][0] / total_words)*100)) + "% in the string" )
