def Primes():
    l = []
    n = int(input("Enter the xber to get primes to: "))

    for x in range(0,n + 1):
       if x > 1:
           for i in range(2,x):
               if (x % i) == 0:
                   break
           else:
               l.append(x)
    return l
print(Primes())
