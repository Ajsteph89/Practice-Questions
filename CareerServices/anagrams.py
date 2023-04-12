# create a function that takes 2 strings and a checks if they are an anagram

def check(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        print("Anagram Detected")
    else:
        print("No Anagram Detected")

check("sector", "escort")