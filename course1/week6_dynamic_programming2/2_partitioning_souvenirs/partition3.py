from sys import stdin


def partition3(values):
    total = sum(values)
    n = len(values)

    # can't split into 3 equal piles unless the total divides by 3
    if n < 3 or total % 3 != 0:
        return 0
    target = total // 3

    # dp[i][j][k] = can the first i souvenirs make pile1 = j and pile2 = k?
    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        v = values[i - 1]
        for j in range(target + 1):
            for k in range(target + 1):
                # souvenir i goes into pile 3 — neither tracked pile changes
                reachable = dp[i - 1][j][k]

                # souvenir i goes into pile 1 — pile 1 was v lower
                if not reachable and j >= v:
                    reachable = dp[i - 1][j - v][k]

                # souvenir i goes into pile 2 — pile 2 was v lower
                if not reachable and k >= v:
                    reachable = dp[i - 1][j][k - v]

                dp[i][j][k] = reachable

    return 1 if dp[n][target][target] else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
