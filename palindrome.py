# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

import re

s = "A man, a plan, a canal: Panama"

def check(pal):
    filter = re.sub(r'(\d+(?:[,.]\d+)+)|[\W_]+', lambda x: x.group(1) if x.group(1) else '', pal).strip()
    nocap = filter.lower()
    return nocap == nocap[::-1]

print(check(s))