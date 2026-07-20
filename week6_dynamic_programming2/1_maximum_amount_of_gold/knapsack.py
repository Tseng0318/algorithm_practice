from sys import stdin


def maximum_gold(capacity, weights):
    n = len(weights)
    
    # dp[i][w] = max weight using first i bars with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # option 1: skip bar i
            dp[i][w] = dp[i-1][w]
            
            # option 2: take bar i (only if it fits)
            if weights[i-1] <= w:
                take = weights[i-1] + dp[i-1][w - weights[i-1]]
                if take > dp[i][w]:
                    dp[i][w] = take
    
    return dp[n][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
