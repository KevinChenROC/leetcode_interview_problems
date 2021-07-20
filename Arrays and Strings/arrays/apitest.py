n = 10
lps1 = [[0] * n for _ in range(n)]  # create lps[n][n]
lps2 = [[0] * n] * n  # create lps[n][n]

print(lps1 == lps2)
