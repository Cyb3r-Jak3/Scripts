import random, os
from datetime import *
import time as t
f_location = (os.getcwd() + '\stuff.txt')
data = []
CA = 0
def Fileread():
	f = open(f_location, 'r')
	r = f.readlines()
	return r
def GenStart():
	f = open(f_location, 'w')
	del data[:]
	data.insert(0, (str(random.randint(0, 100)) + '\n'))
	data.insert(1, '\n')
	del data[2:]
	f.writelines(data)
GenStart()
Completed = False
while 1:
	if (datetime.utcnow().second % 2) == 0:
		if Fileread()[1] == 'Found':
			break
		else:
			CA += 1
			print ('It made it', str(CA), 'cycles')
			GenStart()
			t.sleep(1)