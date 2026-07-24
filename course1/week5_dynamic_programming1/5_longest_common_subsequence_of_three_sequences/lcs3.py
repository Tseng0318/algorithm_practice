def lcs3(a, b, c):
    n, m, q = len(a), len(b), len(c)
    dp = [[[0] * (q+1) for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, q + 1):
                if a[i-1] == b[j-1] == c[k-1]:
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]       # all three match — extend
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])         # drop from one of the three
    
    return dp[n][m][q]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
