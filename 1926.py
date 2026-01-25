maze=[["+",".","+","+","+","+","+"],
      ["+",".","+",".",".",".","+"],
      ["+",".","+",".","+",".","+"],
      ["+",".",".",".","+",".","+"],
      ["+","+","+","+","+",".","+"]]
entrance=[0,1]
m=len(maze)
n=len(maze[0])
visited=[[False] * n for _ in range(m)]

l=0
for i in range(m):
    for j in range(n):
        if maze[i][j]=='.':
            visited[i][j]=True
            l+=1
if l==1:
    print(-1)
visited[entrance[0]][entrance[1]]=False
quequ=[tuple((entrance[0],entrance[1],0))]
while quequ:
    entrance=quequ.pop(0)
    x=entrance[0]
    y=entrance[1]
    time=entrance[2]
    if x+1<m and visited[x+1][y]==True:
        print(1,visited)
        visited[x+1][y]=False
        quequ.append(tuple((x+1,y,time+1)))
    if x-1>=0 and visited[x-1][y]==True:
        print(2, visited)
        visited[x-1][y]=False
        quequ.append(tuple((x-1,y,time+1)))
    if y+1<n and visited[x][y+1]==True:
        print(3, visited)
        visited[x][y+1]=False
        quequ.append(tuple((x,y+1,time+1)))
    if y-1>=0 and visited[x][y-1]==True:
        print(4, visited)
        visited[x][y-1]=False
        quequ.append(tuple((x,y-1,time+1)))
    if (x==m-1 or x==0 or y==n-1 or y==0) and time>0:
        print(x,y,time)
        break
