grid = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]

def proverochka(i, j):
    print('new')
    obch=set()
    for x in range(i,i+3):
        for y in range(j,j+3):
            print(grid[x][y])
            if grid[x][y] in obch or grid[x][y]>=10 or grid[x][y]<1 :
                return 'a',False
            obch.add(grid[x][y])
    for x in range(3):
        if sum(grid[i+x][j:j+3])!=15:
            return 'b',False
        print([grid[i+h][j+x] for h in range(3)])
        if sum([grid[i+h][j+x] for h in range(3)])!=15:
            return 'c',False
    if grid[i][j]+grid[i + 1][j + 1]+grid[i + 2][j + 2]!=15:
        return 'd',False
    if (grid[i][j + 2]+grid[i + 1][j + 1]+grid[i + 2][j])!=15:
        return 'e',False
    return 1
ans=0
for i in range(len(grid)-2):
    for j in range(len(grid[0])-2):

        print(proverochka(i,j))
print(ans)


