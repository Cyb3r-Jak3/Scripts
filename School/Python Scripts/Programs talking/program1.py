import random, os
from datetime import *
import time as t
f_location = (os.getcwd() + '\stuff.txt')
data = []
CA = 0
number1 = random.randint(0, 100)
def Fileread():
	f = open(f_location, 'r')
	r = f.readlines()
	return r
while 1:
	if (datetime.utcnow().second % 2) == 1:
		if int(Fileread()[0]) == number1:
			f = (open(f_location, 'r+'))
			r = f.readlines()
			r[1] = 'Found'
			f.writelines(r)
			break
		else:
			CA += 1
			print ('Made it', str(CA), 'cycles')
			t.sleep(1)