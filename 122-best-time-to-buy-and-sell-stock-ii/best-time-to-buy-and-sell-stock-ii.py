class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if prices==sorted(prices):
            return prices[n-1]-prices[0]
        if prices==sorted(prices,reverse=True):
            return 0
        max_profit=0
        for i in range(1,n):
            if prices[i-1]<prices[i]:
                max_profit = max_profit+ (prices[i]-prices[i-1])
        return max_profit              

        