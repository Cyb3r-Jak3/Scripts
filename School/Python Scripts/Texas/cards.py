def Card(which):
    print ("What is the number or face of", which + "?")
    face = input()
    while face not in ['ace','king','queen','jack','10','9','8','7','6','5','4','3','2']:
        print ('That is not a vaild input. Try Again')
        print ("What is the number of face of", which, '?')
        face = input()

    if face == 'ace':
        num = 14
    elif face == 'king':
        num = 13
    elif face == 'queen':
        num = 12
    elif face == 'jack':
        num = 11
    else:
        num = int(face)
    suit = input("What is the suit of the card? \n")
    while suit not in ['hearts','clubs','spades','diamonds']:
        print ('That is not a valid input')
        suit = input("What is the suit of the card? \n")
    return (num, suit)