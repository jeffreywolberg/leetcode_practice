from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        left = 0
        long_sub = 0
        for right, r_letter in enumerate(s):
            count[r_letter] += 1
            if r_letter in count:
                while(count[r_letter] > 1):
                    count[s[left]] -= 1
                    left += 1
                    
            long_sub = max(right-left+1,  long_sub)
            
        
        return long_sub
                
            
            
        