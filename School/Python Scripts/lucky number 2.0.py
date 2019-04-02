import random
import time
rand1, rand2, rand3 = [int(x) for x in input("Enter three numbers between 1-99 here: ").split()]
rand11 = 0
t_t1 = 0
rand22 = 0
t_t2 = 0
rand33 = 0
t_t3 = 0
while rand1 != rand11:
        rand11 = random.randint(0,99)
        t_t1 = t_t1 +1
while rand2 != rand22:
        rand22 = random.randint(0,99)
        t_t2 = t_t2 +1
while rand3 != rand33:
        rand33 = random.randint(0,99)
        t_t3 = t_t3 +1
                

print ("It took " + str(t_t1) + " tries to get " + str(rand1))
print ("It took " + str(t_t2) + " tries to get " + str(rand2))
print ("It took " + str(t_t3) + " tries to get " + str(rand3))
