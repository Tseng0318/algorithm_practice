def edit_distance(a, b):
    n, m = len(a), len(b)
    
    # dp[i][j] = edit distance between a[:i] and b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # base cases: the first row and first column
    for i in range(n + 1):
        dp[i][0] = i          # a[:i] → empty string
    for j in range(m + 1):
        dp[0][j] = j          # empty string → b[:j]
    
    # fill the rest of the grid
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]                # characters match — free
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1] ,     # substitute
                    dp[i-1][j] ,     # delete from a
                    dp[i][j-1]      # insert into a
                )
    
    return dp[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
