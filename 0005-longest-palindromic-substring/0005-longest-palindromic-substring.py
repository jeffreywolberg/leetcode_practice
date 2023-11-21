class Solution:
    
    def print_array(self, a):
        for row in a:
            print(row)
            
#     def longestPalindrome(self, s: str) -> str:
#         # 2D table where a[i,j]  represents length of longest palindrome from i to j
#         a = [[0 for _ in range(len(s))] for _ in range(len(s))]
#         for l in range(1, len(s)+1):
#             for i in range(0, len(s)-l+1):
#                 j = i + l - 1
#                 if l == 1:
#                     a[i][j] = 1
#                 elif l == 2:
#                     a[i][j] = 1 if s[i] == s[j] else 0
#                 else:
#                     a[i][j] = 1 if a[i+1][j-1] and s[i] == s[j] else 0
#         # self.print_array(a)
        
#         for l in range(len(s), 0, -1):
#             for i in range(0, len(s)-l+1):
#                 j = i+l-1
#                 if a[i][j]:
#                     return s[i:j+1]

    def longestPalindrome(self, s: str) -> str:
        # Transform the string to put '#' between each character and at the ends.
        # This helps to handle both odd and even length palindromes uniformly.
        T = '#' + '#'.join(s) + '#'
        n = len(T)
        P = [0] * n  # Array to store the length of the palindrome at each center.
        C = R = 0  # Current center and right boundary.

        for i in range(n):
            mirror = 2 * C - i  # Mirror of the current position i.

            # Check if the current position is within the right boundary.
            if i < R:
                P[i] = min(R - i, P[mirror])

            # Attempt to expand the palindrome centered at i.
            a, b = i + P[i] + 1, i - P[i] - 1
            while a < n and b >= 0 and T[a] == T[b]:
                P[i] += 1
                a += 1
                b -= 1

            # If the palindrome centered at i expands past R, adjust the center and R.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the longest palindrome in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]
            
        
        
        
        