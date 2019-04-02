import random, os, pygame, sys
pygame.init()
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
def Update():
    pygame.display.flip()
def pygameSetup():
    global screen,font,win,again,stage
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)
    pygame.display.set_caption("HANGMAN")
    font = pygame.font.SysFont('Calibri', 25, True, False)
    level = 1
    stage = pygame.image.load("stage"+str(level)+".png")
    screen.blit(stage,(0,0))
    win = pygame.image.load("win.png")
    again = pygame.image.load("again.png")
    Update()

def setup():
    global words
    choice = input("What catergory do you want to choose from: Animals, Countries or States? ").lower()
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
pygameSetup()
mLetters = ''
cLetters = ''
secretWord = getRandomWord(words)
gameDone = False
blanks = '_|' * len(secretWord)
hpy = '-'
word_guess = 1
space = secretWord.find(hpy)
def Board(mLetters, cLetters, secretWord):
    print()
    blanks = '_' * len(secretWord)
    space = secretWord.find(hpy)
    if hpy in secretWord:
        blanks = blanks[:space] + hpy + blanks[space+1:]
        cLetters = cLetters + hpy
    if word_guess == 1:
        print( 'Type "word" to guess the word \n' 'You only have 1 guess')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in cLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')

    #for i in range(len(secretWord)):
    #    pygame.draw.line(screen, BLACK, (100+(i*5),480), (110+(i*5),480), 2)
    Word = "Word: " + blanks  
    level = len(mLetters) + 1
    screen.blit(font.render(Word, True, BLACK), [100, 400])
    textMissed = "Missed Letters:" + mLetters   
    screen.blit(font.render(textMissed, True, RED), [100, 350])
    #lettersleft = len(secretWord) - len(cLetters)
    #screen.blit(font.render(str(lettersleft), True, GREEN), [300, 400])
    print()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
    Update()
def getGuess(alreadyGuessed):
    while True:
        global word_guess
        print('Guess a letter.')
        guess = input()
        if len(guess) != 1:
            if guess == 'word' and word_guess == 1:
                guess = input("What is your final guess? ").lower()
                if guess == secretWord:
                    return guess
                    break
                elif guess != secretWord:
                    print('Not the correct word')
                    word_guess = 0
            elif word_guess == 0:
                print('You have already used your word attempt') 
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    choice = input('Do you want to play again? (yes or no)')
    if choice.lower().startswith('y'):
        choice = input('Do you want a different catergory? (yes or no)')
        if choice.lower().startswith('y'):
            return 1
        elif choice.lower().startswith('n'):
            return 2

    else:
        return 0
    return
while True:
    Board(mLetters, cLetters, secretWord)
    guess = getGuess(mLetters + cLetters)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
    clock.tick(30)
    level = len(mLetters) + 1
    stage = pygame.image.load("stage"+str(level)+".png")
    screen.blit(stage, (0,0))
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
            screen.blit(win,(0,0))
            Update()
            print('Yes! The word is "' + secretWord + '"! You have won!')
            gameDone = True
    else:
        mLetters = mLetters + guess
        
    if len(mLetters) == 6:
        Board(mLetters, cLetters, secretWord)
        screen.blit(again,(0,0))
        Update()
        print('You have run out of guesses!\nAfter ' + str(len(mLetters)) + ' missed guesses and ' + str(len(cLetters)) + ' correct letters, the word was "' + secretWord + '"')
        gameDone = True
    if gameDone == True:
        fchoice = playAgain()
        if fchoice == 2:
            mLetters = ''
            cLetters = ''
            secretWord = getRandomWord(words)
            gameDone = False
        elif fchoice == 1:
            mLetters = ''
            cLetters = ''
            setup()
            secretWord = getRandomWord(words)
            gameDone = False
        elif fchoice == 0:
            pygame.quit()
            sys.exit()

    if len(mLetters) == 0:
        level = 1
    else:
        level = len(mLetters) + 1
    lettersleft = len(secretWord) - len(cLetters)
    screen.blit(font.render("There are "+ str(lettersleft)+" letters left", True, GREEN), [300, 400])
    stage = pygame.image.load("stage"+str(level)+".png")
    screen.blit(stage, (0,0))
    textMissed = "Missed Letters:" + mLetters   
    screen.blit(font.render(textMissed, True, RED), [100, 350])
    Update()

