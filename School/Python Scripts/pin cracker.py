import random
import time
p = 1
ppl = 0
pinc = 1000
pint = []
file = open("C:\\Users\\Jacob\\Google Drive\\Python\\pinnumbers.txt", 'r')
text = file.read()
pil = list(text.split())
st = time.time()
def getPin(pinlist):
    pinIndex = random.randint(0, len(pinlist) - 1)
    return pinlist[pinIndex]
def method2(tpin):
    global ppl
    while tpin != ppl:
        if tpin != ppl:
            ppl = random.randint(0, 9)
            print(ppl)
    return tpin
pin = getPin(pil)
print ('Here is the start', pin)
method = int(input('Choose your method: Brute Force all (1) or Brute Force each digit (2): '))
if method == 1:
    while pin != pinc:
        pinc = random.randint(1000,9999)
    


elif method == 2:
    while pint != pin:
        p1, p2, p3, p4 = list(pin)
        while p1 != ppl:
            ppl = random.randint(0, 9)
        while p2 != ppl:
            ppl = random.randint(0, 9)
        while p3 != ppl:
            ppl = random.randint(0, 9)
        while p4 != ppl:
            ppl = random.randint(0, 9)
        pint = [p1 + p2 + p3 + p4]
        pin = [pin]
        print(pint)
        print(pin)
        if pint == pin:
            print('Solved')

print('Method complete')
if method == 1:
    print (pinc)
if method == 2:
    print(p1, p2, p3, p4)
