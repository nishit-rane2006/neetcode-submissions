class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        for i in range(len(prices)-1):
            p = max(p, max(prices[i+1:])-min(prices[:i+1]))
        return p