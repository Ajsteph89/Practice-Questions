# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

s = "There's-a-starman-waiting-in-the-sky"
k = 3

def caesarCipher(s, k):
    answer = ""

    for i in range(len(s)):
        char = s[i]
        # check uppercase
        if (char.isupper()):
            answer += chr((ord(char) + k - 65) % 26 + 65)
        # check for non letter
        elif not char.isalpha():
            answer += char
        # anything else should be a lowercase letter
        else:
            answer += chr((ord(char) + k - 97) % 26 + 97)
    
    print(answer)

caesarCipher(s, k)