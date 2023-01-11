# write a function that prints out the first 10 numbers in the Fibonacci sequence


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,


sequence = [0, 1]
s = 0

def get_sequence(sequence, s):
    while len(sequence) < 10:
        for x in range(1, len(sequence)):
            s= sequence[x-1] + sequence[x]
        sequence.append(s)
    print(sequence)

get_sequence(sequence, s)