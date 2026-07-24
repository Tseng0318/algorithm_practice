def lcs2(a, b):
    n, m = len(a), len(b)
    
    # dp[i][j] = length of LCS of a[:i] and b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # base cases are already 0 from the allocation — nothing to seed
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 +  dp[i-1][j-1]             # match — extend the LCS
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])             # mismatch — best of dropping one side
    
    return dp[n][m]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
