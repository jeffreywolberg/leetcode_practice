from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long_sub = ""
        count = Counter()
        max_freq = 0
        left = 0
        for i, l in enumerate(s):
            count[l] += 1
            if count[l] > max_freq:
                max_freq = count[l]
            
            if i - left + 1 > max_freq + k:
                count[s[left]] -= 1
                left += 1
            else:
                long_sub = s[left: i+1]
                
        
        return len(long_sub)
            
            
            
            
                
            
        
        
        return longest_sub
                    
        