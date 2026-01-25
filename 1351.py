grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
ans=j=0
i=len(grid)-1
while i>=0 and j<=len(grid[0])-1:
    if grid[i][j]<0:
        i-=1
        ans+=len(grid[0])-j
        j=0
    else:
        j+=1
print(ans)
