# Given a string s, return the longest 
# palindromic substring in s.

input = "BABAD"

new = []

for x in range(len(input)):
    for y in range(x, len(input)+1):
        piece = input[x:y]
        if piece == piece[::-1] and len(piece)>1:
            new.append(piece)

new.sort()

if len(new) == 0:
    print('None')
else:
    print(max(new, key=len))
