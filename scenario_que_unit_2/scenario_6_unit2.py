# Number of Ways to Make Change

def count_ways(coins, target):
    # Create DP table
    dp = [0] * (target + 1)

    # There is one way to make amount 0: use no coins
    dp[0] = 1

    # Dynamic Programming
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]


# Accept coin denominations
coins = list(map(int, input("Enter coin denominations: ").split()))

# Accept target amount
target = int(input("Enter target amount: "))

# Calculate number of combinations
ways = count_ways(coins, target)

# Display result
print("Total possible combinations:", ways)


# OUTPUT:
# Enter coin denominations: 1 2 5
# Enter target amount: 5
# Total possible combinations: 4
#
# The 4 combinations are:
# 5
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1