def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find included items
    items, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i)
            w -= weights[i - 1]

    return dp[n][capacity], items[::-1]


# Execution & Formatting
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

print("0/1 KNAPSACK PROBLEM")

print("Items:")
for i in range(len(weights)):
    print(f"Item {i + 1}: Weight = {weights[i]}, Value = {values[i]}")

max_val, selected_items = knapsack_bottom_up(weights, values, capacity)

print(f"\nKnapsack Capacity: {capacity}")
print(f"Maximum Value: {max_val}")
print(f"Selected Items: {selected_items}")

#Output
#0/1 KNAPSACK PROBLEM

#Items:
#Item 1: Weight = 2, Value = 12
#Item 2: Weight = 1, Value = 10
#Item 3: Weight = 3, Value = 20
#Item 4: Weight = 2, Value = 15

#Knapsack Capacity: 5
#Maximum Value: 37
#Selected Items: [1, 2, 4]

