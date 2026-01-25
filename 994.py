
appelsi=[[2,1,1],[1,1,0],[0,1,1]]
q=[]
m=len(appelsi[0])
n=len(appelsi)
vis=[[False]*len(appelsi[0]) for i in range(len(appelsi))]
for i in range(len(appelsi)):
    for j in range(len(appelsi[0])):
        if appelsi[i][j]==2:
            q.append(((i,j),0))

print(q)
print(vis)
ans=0
while q:
    (i,j),time=q.pop(0)
    print(i,j,time)
    print(q)
    ans=max(ans,time)
    # top
    if i - 1 >= 0 and not vis[i - 1][j] and appelsi[i - 1][j] == 1:
        vis[i - 1][j] = True
        q.append(((i - 1, j), time + 1))
    # right
    if j + 1 < m and not vis[i][j + 1] and appelsi[i][j + 1] == 1:
        vis[i][j + 1] = True
        q.append(((i, j + 1), time + 1))
    # bottom
    if i + 1 < n and not vis[i + 1][j] and appelsi[i + 1][j] == 1:
        vis[i + 1][j] = True
        q.append(((i + 1, j), time + 1))
    # left
    if j - 1 >= 0 and not vis[i][j - 1] and appelsi[i][j - 1] == 1:
        vis[i][j - 1] = True
        q.append(((i, j - 1), time + 1))
    for i in range(n):
        for j in range(m):
            if appelsi[i][j]==1 and not vis[i][j]:
                print(-1)
    return ans




