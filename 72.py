def levenshteinFulMatrix(str1,str2):
    m=len(str1)
    n=len(str2)
    ans=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        ans[i][0]=i
    for j in range(n+1):
        ans[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                print(str1[i - 1], str2[j - 1])
                ans[i][j]=ans[i-1][j-1]
            else:
                ans[i][j]=1+min(ans[i-1][j-1],ans[i-1][j],ans[i][j-1])
    for i in ans:
        print(i)
    return ans[m][n]
print(levenshteinFulMatrix('kitten','sitting'))
