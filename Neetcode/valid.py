
inputStr = ['(90,180)','(+90,+190)', '(90.180)' ]
def funcValidPairs(inputStr):
    Map = [' ', ]
    for x in inputStr:
        for y in x:
            if y.isalpha:
                return False

	# 		if y in Map:
	# 			return False
	# 		elif any(c.isalpha() for c in s)
	# return
    #     return not stack


print(funcValidPairs(inputStr))