import re
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        isalnum = lambda s: s.isalnum()
        s = list(filter(isalnum, s))
        i = 0
        j = len(s) - 1
        while(i < j):
            if s[i] != s[j]:
                print(i, j, s[i], s[j])
                return False
            i += 1
            j -= 1
        
        return True
        