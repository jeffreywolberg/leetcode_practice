class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        left = 0
        for i, p in enumerate(prices):
            if p-prices[left] > maxProf:
                maxProf = p-prices[left]
            if p < prices[left]:
                left = i
            
        return maxProf
