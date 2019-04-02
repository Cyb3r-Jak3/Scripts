heads = 35
legs = 94
def math(h, l):
    for rab in range(h+1):
        chi = h - rab
        if 2 * chi + 4 * rab == l:
            return chi, rab
    
results = math(heads, legs)
print("There are %d chickens and %d rabbits" % results)
