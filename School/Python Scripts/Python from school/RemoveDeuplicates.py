def remove(l):
    s = []
    for i in l:
        if i not in s:
            s.append(i)
    return s
l = [1,2,2,3,3,3,4,4,4,4,5,5,6,6,7,5,54,6,4,4,7,4,5,6,6,]
print (remove(l))
