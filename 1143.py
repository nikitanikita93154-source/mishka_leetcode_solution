text1='abcde'
text2='ace'
n=len(text1)
m=len(text2)
ans=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if text1[j-1]==text2[i-1]:
            ans[i][j]=ans[i-1][j-1]+1
        else:
            ans[i][j]=max(ans[i-1][j],ans[i][j-1])
print(ans)