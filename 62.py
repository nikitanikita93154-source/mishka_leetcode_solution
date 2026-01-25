m=3
n=7
ans=[[0]*(n) for _ in range(m)]


print(ans)
for i in range(m):
    for j in range(n):
        if j-1<0 or i-1<0:
            ans[i][j]=1
        else:
            ans[i][j]=ans[i-1][j]+ans[i][j-1]
print(ans)
