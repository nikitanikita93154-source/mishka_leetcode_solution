grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
zer=[0]*len(grid)
max_Right=0
for i in range(len(grid)):
    j=len(grid[0])-1
    while j>=0 and grid[i][j]!=1:
        zer[i]+=1
        j-=1
        max_Right=max(max_Right,zer[i])
j=len(grid)-1
for i in range(len(grid)):
    if zer[i]<j:
        print(-1)
    j-=1
print(zer)
ans=0
for i in range(len(grid)):
    sort=False
    for j in range(0,len(grid)-i-1):
        if zer[j]<zer[j+1]:
            ans+=1
            zer[j],zer[j+1]=zer[j+1],zer[j]
            sort=True

    if sort==False:
        break
print(zer)
print(ans)
