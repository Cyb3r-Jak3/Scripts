from cards import *
from findwin import *
#Gets the cards
'''hand1 = Card('the first card in your hand')
hand2 = Card('the second card in your hand')
table1 = Card('the first card on the table')
table2 = Card('the second card on the table')
table3 = Card('the third card on the table')
table4 = Card('the fourth card on the table')
table5 = Card('the fifth card on the table')'''
hand1 = (5, 'hearts')
hand2 = (7, 'diamonds')
table1 = (14, 'spades')
table2 = (4, 'spades')
table3 = (13, 'hearts')
table4 = (8, 'clubs')
table5 = (5, 'hearts')
#organizes the cards into their groups no use for this as of now
full_table = [table1, table2, table3, table4, table5]
full_hand = [hand1, hand2]
win_kind = Find(hand1,hand2,table1,table2,table3,table4,table5)
print (win_kind)