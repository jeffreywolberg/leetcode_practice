from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        start = 0
        long_sub_len = 0
        left = 0
        for r, l in enumerate(s):
            count[l] += 1
            
            while count[l] > 1:
                count[s[left]] -= 1
                left += 1
            
            long_sub_len = max(long_sub_len, r - left + 1)
            
        return long_sub_len
                
            
            
        