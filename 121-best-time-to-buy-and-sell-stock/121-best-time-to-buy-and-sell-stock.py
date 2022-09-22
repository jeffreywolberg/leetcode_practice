class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minP = math.inf
        
        for i in range(len(prices)):
            if prices[i] < minP:
                minP = prices[i]
            elif prices[i] - minP > maxProf:
                maxProf = prices[i] - minP
            
        return maxProf
            
