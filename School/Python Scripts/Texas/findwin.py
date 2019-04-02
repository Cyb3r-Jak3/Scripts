def Find(hand1,hand2,table1,table2,table3,table4,table5):
	win_kind = ''
	if  hand1[0] == hand2[0] :
		if hand1[0] in [table1[0], table2[0], table3[0], table4[0], table5[0] ] :
			return '3 of a kind'
	if hand1[0] in [ table1[0], table2[0], table3[0], table4[0], table5[0]]:
		return 'pair1'
	if hand2[0] in [ table1[0], table2[0], table3[0], table4[0], table5[0] ]:
		return 'pair2'
	if hand2[0] in [ table1[0], table2[0], table3[0], table4[0], table5[0] ] and win_kind == 'pair1':
		return 'two pair'