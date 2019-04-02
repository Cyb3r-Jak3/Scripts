import random
import string
word = input("Choose a 5 letter word: ")
l = list(word)
for (index, letter) in enumerate(word):
  l[index] = letter
g1 = 'z'
for (index, letter) in enumerate(word):
  g1[index] = letter


if l[1] != None:
     if l[1] != g1:
          while l[1] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g11 = g11 + 1
               
if l[2] != None:
     if l[2] != g1:
          while l[2] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g22 = g22 + 1
if l[3] != None:          
     if l[3] != g1:
          while l[3] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g33 = g33 + 1
if l[4] != None:
     if l[4] != g1:
          while l[4] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g44 = g44 + 1
if l[5] != None:
     if l[5] != g1:
          while l[5] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g55 = g55 + 1
if l[6] != None:
     if l[6] != g1:
          while l[6] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g66 = g66 + 1
if l[7] != None:
     if l[7] != g1:
          while l[7] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g77 = g77 + 1
if l[8] != None:     
     if l[8] != g1:
          while l[8] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g88 = g88 + 1
if l[9] != None:     
     if l[9] != g1:
          while l[9] != g1:
               g1 = random.choice(string.ascii_lowercase)
               g99 = g99 + 1
print ("Over")          

print ("It took " + str(g11) + " tries to get " + str(l[1]))
print ("It took " + str(g22) + " tries to get " + str(l[2]))
print ("It took " + str(g33) + " tries to get " + str(l[3]))
print ("It took " + str(g44) + " tries to get " + str(l[4]))
print ("It took " + str(g55) + " tries to get " + str(l[5]))
print ("It took " + str(g66) + " tries to get " + str(l[6]))
print ("It took " + str(g77) + " tries to get " + str(l[7]))
print ("It took " + str(g88) + " tries to get " + str(l[8]))
print ("It took " + str(g99) + " tries to get " + str(l[9]))
