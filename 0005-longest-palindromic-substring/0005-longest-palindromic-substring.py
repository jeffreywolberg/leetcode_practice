

class Solution:
    def helper(self, s, odd=True):
        res = ""
        resLen = 0
        
        for i in range(0, len(s)):
                l, r = i, (i if odd else i+1)
                while (l >= 0 and r < len(s) and s[l] == s[r]):
                    leng = r-l+1
                    if leng > resLen:
                        res = s[l:r+1]
                        resLen = leng
                    r += 1
                    l -= 1
        return res
    
    def longestPalindrome(self, s: str) -> str:
        
#         dp = [[(-1, -1) for j in range(len(s))] for i in range(len(s))]
        
#         for i in range(len(s)):
#             dp[i][i] = (i, i)
#         for j in range(1, len(s)):
#             i = j-1
#             dp[i][j] = (i, j) if s[i] == s[j] else (i, i)
        
#         for l in range(3, len(s)+1):
#             for i in range(len(s)-l+1):
#                 j = i + l - 1
#                 opt1 = leng(dp[i][j-1])
#                 opt2 = leng(dp[i+1][j])
#                 opt3 = leng(dp[i+1][j-1]) + (2 if (s[i] == s[j]) else 0)
                
#                 max_v = max(opt1, opt2, opt3)
#                 if opt1 == max_v:
#                     dp[i][j] = dp[i][j-1]
#                 elif opt2 == max_v:
#                     dp[i][j] = dp[i+1][j]
#                 else:
#                     dp[i][j] = (i, j)
             
#         v = dp[0][len(s)-1]
#         return s[v[0]:v[1]+1]
    
        opt1 = self.helper(s, odd=True)
        opt2 = self.helper(s, odd=False)
        if len(opt1) > len(opt2):
            return opt1
        return opt2
        
        
            
            
                
                
                
                    
                
            
            
        
        
        