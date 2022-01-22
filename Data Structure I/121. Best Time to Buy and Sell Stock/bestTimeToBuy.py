class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        potentialProfit = prices[1] - prices[0]
        buyIn = prices[0]

        for price in range(len(prices)):
            buyIn = min(prices[price], buyIn)
            potentialProfit = max(potentialProfit, prices[price] - buyIn)
        
        return potentialProfit



check = Solution()
print(check.maxProfit(prices=[7,6,4,3,1]))