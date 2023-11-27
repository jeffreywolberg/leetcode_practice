

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = ""
        substr = ""
        i = 0
        j = 0 # inclusive
        letter_set = set()
        
        while i < len(s) and j < len(s):
            if s[j] not in letter_set:
                letter_set.add(s[j])
                j += 1
                if j-i > len(longest_substr):
                    longest_substr = s[i:j]
            else:
                popped_c = s[i]
                letter_set.remove(s[i])
                i += 1
                while i < len(s) and popped_c != s[j]:
                    popped_c = s[i]
                    letter_set.remove(s[i])
                    i += 1
                
        return len(longest_substr)
            
                
        
        