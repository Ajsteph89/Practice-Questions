# determine the index of a letter in the given string that could be removed to make the string a palindrome

s = "aaab"


def palindromeIndex(s):
    # check if initial s is a palindrome
    if s == s[::-1]:
        return -1
    
    n = len(s)

    # iterate through half the string 
    for i in range(n//2):
        # check if first and last characters are diff
        if s[i] != s[n-1-i]:
            # check if everything around the diff character is a palindrome
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-1-i
            elif s[i+1:n-i] == s[i +1:n-i][::-1]:
                return i
    return -1 #no other statements return a value

print(palindromeIndex(s))

