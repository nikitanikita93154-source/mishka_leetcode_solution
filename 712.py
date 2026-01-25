s1='delete'
s2='leet'

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + ord(s1[j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
s=sum([ord(i) for i in (s1+s2)])
print(s)
print(s-lcs(s1,s2)*2)
