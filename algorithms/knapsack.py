
def knapsack(parcels, capacity):
    n = len(parcels)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = parcels[i - 1]["Weight"]
        value = parcels[i - 1]["Value"]

        for w in range(capacity + 1):

            dp[i][w] = dp[i - 1][w]

            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - weight]
                )

    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["Weight"]

    selected.reverse()

    return selected, dp[n][capacity]
