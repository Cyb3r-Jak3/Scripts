import random
file = open("C:\\Users\\Jacob\\Google Drive\\Python\\pinnumbers.txt", 'r')
text = file.read()
pil = list(text.split())
def getPin(pinlist):
    pinIndex = random.randint(0, len(pinlist) - 1)
    return pinlist[pinIndex]
pin = getPin(pil)
p1, p2, p3, p4 = [int(x) for x in pin]
p11, p22, p33, p44 = 1, 2, 3, 4
print (pin)
print (p1, p2, p3, p4)
print (p11, p22, p33, p44)

