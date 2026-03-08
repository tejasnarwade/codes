class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # jar prices acending sorted ahet tr day0 price is least and day n-1 prices is largest henece max profit if day n-1 - day 0
        if prices==sorted(prices):
            return prices[n-1]-prices[0]
        #jar prices descending order madhe sorted ahet tr maxPrice day 0 la asnar hence we will not sell as it will make us loss mang return - as we willl n ot buy
        if prices==sorted(prices,reverse=True):
            return 0
        #ithe apan chheck karnar i -> n-1 if prices[i-1] < prices[i] we sell and take position as profit
        max_profit=0
        for i in range(1,n):
            if prices[i-1]<prices[i]:
                max_profit = max_profit+ (prices[i]-prices[i-1])
        return max_profit
        #as at each step we are booking profit if previous price is smaller this is greedy algo

        