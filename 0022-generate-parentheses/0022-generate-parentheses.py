class Solution:
    def genParen(self, cur, n_o, n_c, n, l):
        if n_c > n_o:
            return
        if n_o > n:
            return
        elif n_o == n_c == n:
            l.append(cur)
        
        self.genParen(cur + "(", n_o+1, n_c, n, l)
        self.genParen(cur + ")", n_o, n_c+1, n, l)
            
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        self.genParen("", 0, 0, n, l)
        return l
        
        