def coins(n, d):
    d = list(reversed(d))
    len_d = len(d)
    k = [0] * len_d
    r = n
    for i in range(len_d):
        if r < d[i]:
            k[i] = 0
            continue
        else:  
            k[i] = r // d[i]
            r -= k[i] * d[i]
    return k

print(coins(140, [50, 25, 10, 5, 1]))

def grid_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

print(grid_paths(3, 4))
