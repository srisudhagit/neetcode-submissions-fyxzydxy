class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [amount + 1] * (amount + 1)
        DP[0] = 0
        for part in range(1, amount+1):
            for coin in coins:
                if part-coin >= 0:
                    DP[part] = min(DP[part] , DP[part-coin] + 1)
                
        return DP[amount] if DP[amount] != amount+1 else -1