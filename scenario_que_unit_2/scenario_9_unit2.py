# Number of Ways to Make Change 

class CoinChange:
    def __init__(self, coins, amount):
        self.coins = coins
        self.amount = amount

    def count_ways(self):
        dp = [0] * (self.amount + 1)
        dp[0] = 1

        for coin in self.coins:
            for i in range(coin, self.amount + 1):
                dp[i] += dp[i - coin]

        return dp[self.amount]


# Input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

# Object creation
obj = CoinChange(coins, amount)

print("Total possible combinations:", obj.count_ways())


# OUTPUT:
# Enter coin denominations: 1 2 5
# Enter target amount: 5
# Total possible combinations: 4