

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        letter_set = set()
        
        for r in range(len(s)):
            while s[r] in letter_set:
                letter_set.remove(s[l])
                l += 1
        
            letter_set.add(s[r])
            res = max(r-l+1, res)
        return res
            
                
        
        