import re
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        s = s.translate(str.maketrans('', '', string.punctuation+' '))
        i = 0
        j = len(s) - 1
        while(i < j):
            if s[i] != s[j]:
                print(i, j, s[i], s[j])
                return False
            i += 1
            j -= 1
        
        return True
        