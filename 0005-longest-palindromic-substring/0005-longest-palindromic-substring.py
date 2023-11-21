class Solution:
    
    def print_array(self, a):
        for row in a:
            print(row)
            
    def longestPalindrome(self, s: str) -> str:
        # 2D table where a[i,j]  represents length of longest palindrome from i to j
        a = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for l in range(1, len(s)+1):
            for i in range(0, len(s)-l+1):
                j = i + l - 1
                if l == 1:
                    a[i][j] = 1
                elif l == 2:
                    a[i][j] = 1 if s[i] == s[j] else 0
                else:
                    a[i][j] = 1 if a[i+1][j-1] and s[i] == s[j] else 0
        # self.print_array(a)
        
        for l in range(len(s), 0, -1):
            for i in range(0, len(s)-l+1):
                j = i+l-1
                if a[i][j]:
                    return s[i:j+1]
            
        
        
        
        