import random
rand1 = int(input("Pick a number between 1 and 99 "))
rand11 = 0
t_t1 = 0
rand2 = int(input("Pick another number between 1 and 99 "))
rand22 = 0
t_t2 = 0
rand3 = int(input("Pick a third number between 1 and 99 "))
rand33 = 0
t_t3 = 0
while rand1 != rand11:
        rand11 = random.randint(0,99)
        if rand11 == rand1:
                print ("Success")
        else:
                t_t1 = t_t1 +1
while rand2 != rand22:
        rand22 = random.randint(0,99)
        if rand22 == rand2:
                print ("Success")
        else:
                t_t2 = t_t2 +1
while rand3 != rand33:
        rand33 = random.randint(0,99)
        if rand33 == rand3:
                print ("Success")
        else:
                t_t3 = t_t3 +1
                

print ("It took " + str(t_t1) + " tries to get " + str(rand1))
print ("It took " + str(t_t2) + " tries to get " + str(rand2))
print ("It took " + str(t_t3) + " tries to get " + str(rand3))
