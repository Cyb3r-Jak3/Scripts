def CardType(which):
    print ('What is the number or face of', which, '?')
    face = input()
    if face not in ['ace','king','queen','jack','10','9','8','7','6','5','4','3','2']:
        print ('That is not a vaild input. Try Again')
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
    if suit not in ['hearts','clubs','spades','diamonds']:
        print ('That is not a valid input')
    return (num, suit)


FH = CardType("first card in hand")
SH = CardType("second card in hand")
FT = CardType("first card on the table")
ST = CardType("second card on the table")
TT = CardType("third card on the table")
FOT = CardType("forth card on the table")
FIT = CardType("fifth card on the table")
hand = [FH, SH]
table = [FT, ST, TT, FOT, FIT]

if FH[0] or SH[0] == FT[0] or ST[0] or TT[0] or FOT[0] or FIT[0]:
    print ('You have a pair')
