import random, os
PICS = ['''
  
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
ENDING = ['''

00000   000    0   0      0    00000    0   00000  0     0
  0     0  0    0 0      0 0   0       0 0    0    0 0   0
  0     000      0      00000  0  00  00000   0    0  0  0
  0     0  0     0      0   0  0   0  0   0   0    0   0 0
  0     0  0     0      0   0  00000  0   0 00000  0     0
    ''', '''

00000  00000  00000  000      00000  00000   000
0      0   0  0   0  0  0       0    0   0   0  0
0  00  0   0  0   0  0   0      0    0   0   000
0   0  0   0  0   0  0  0     0 0    0   0   0  0
00000  00000  00000  000      000    00000   000  

''']
def setup():
    global words
    choice = raw_input("What catergory do you want to choose from: Animals, Countries or States? ").lower()
    if choice.startswith('a'):
        file = open (os.getcwd() + "\\animals.txt", 'r')
    if choice.startswith('s'):
        file = open (os.getcwd() + "\\states.txt", 'r')
    if choice.startswith('c'):
        file = open (os.getcwd() + "\\countries.txt", 'r')
    text = file.read().lower()
    words = list(text.split())

        
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
setup()
print('H A N G M A N')
mLetters = ''
cLetters = ''
secretWord = getRandomWord(words)
gameDone = False
blanks = '_' * len(secretWord)
hpy = '-'
space = secretWord.find(hpy) 
def Board(PICS, mLetters, cLetters, secretWord):
    print(PICS[len(mLetters)])
    print
    blanks = '_' * len(secretWord)
    space = secretWord.find(hpy)
    if hpy in secretWord:
        blanks = blanks[:space] + hpy + blanks[space+1:]
        cLetters = cLetters + hpy
    print 'Missed letters:',
    for letter in mLetters:
        print letter,
    print
 
    blanks = '_' * len(secretWord)
 
    for i in range(len(secretWord)):
        if secretWord[i] in cLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
 
    for letter in blanks:
        print letter,
    print

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            if guess =='word':
                guess = raw_input("What is your final guess? ").lower()
                if guess == secretWord:
                    return guess
                    break
                else:
                    print('Not the correct word')
            else:
                print('Not the correct word')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz-':
            print('Please enter a LETTER.')
        else:
            return guess
 
def playAgain():
    print('Do you want to play again? (yes or no)')
    if raw_input().lower().startswith('y'):
        print('Do you want a different catergory? (yes or no)')
        if raw_input().lower().startswith('y'):
            return 2
        else:
            return 1
    else:
        return 0


while True:
    Board(PICS, mLetters, cLetters, secretWord)
    guess = getGuess(mLetters + cLetters)
    if hpy in secretWord:
        blanks = blanks[:space] + hpy + blanks[space+1:]
        cLetters = cLetters + hpy
    if guess in secretWord:
        cLetters = cLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in cLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(ENDING[1])
            print('Yes! The word is "' + secretWord + '"! You have won!')
            gameDone = True
    else:
        mLetters = mLetters + guess
        
        if len(mLetters) == len(PICS) - 1:
                Board(PICS, mLetters, cLetters, secretWord)
                print(ENDING[0])
                print('You have run out of guesses!\nAfter ' + str(len(mLetters)) + ' missed guesses and ' + str(len(cLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameDone = True
    if gameDone == True:
        c = playAgain()
        if c == 1:
            mLetters = ''
            cLetters = ''
            gameDone = False
            secretWord = getRandomWord(words)
            print ('H A N G M A N')
        elif c == 2:
            mLetters = ''
            cLetters = ''
            gameDone = False
            setup()
            secretWord = getRandomWord(words)
            print ('H A N G M A N')
        else:
            break
