word = 'MadamImAdam'

def check(word):
    word = word.lower()
    return word == word[::-1]

print(check(word))