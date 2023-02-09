# reverse column 2
# reverse row 0 
# sum values in upper left quad

matrix = [
    [112, 42, 83, 119], 
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]


length = len(matrix)

for i in range(length):
    matrix[i][-2]

print(matrix)


# row 0 column 2
# row 3 column 2
# matrix[0][2] = matrix[3][2]

# matrix[0]= matrix[0][::-1]


# print((matrix[0][1]))
# print((matrix[1][0]))
# print(matrix[1][1]+matrix[1][0]+matrix[0][1]+matrix[0][0])

# for x in range(len(matrix)):
#     matrix[x].sort(reverse=True)
#     print(matrix[x])
        