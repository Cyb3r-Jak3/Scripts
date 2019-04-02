import random
import string
word = input("Choose a 5 letter word: ").lower()
l = list(word)
g = len(word)
z = 'z'
for (index, letter) in enumerate(word):
  l[index] = letter
for i in range(len(word)):
  g[i] = range(len(word))

for i in range(int(len(word))):
  if l[i] != None:
     if l[i] != z:
          while l[i] != z:
               z = random.choice(string.ascii_lowercase)
               g[i] += 1
               
               


for i in range(len(word)):
  print ("It took " + "blank" + " tries to get: " + str(l[i]))
