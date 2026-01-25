connections = [[4,5],[0,1],[1,3],[2,3],[4,0]]
visited=set()
ans=0
def dfs(num,node,ans):

    if num in connections[node]:
        visited.add(node)
        print(visited)
        if num==connections[node][0]:
            if node+1==len(connections):
                return ans+1
            return dfs(connections[node][1],node+1,ans+1)
        else:
            if node+1==len(connections):
                return ans
            return dfs(connections[node][0], node + 1, ans)
    else:
        return ans
for i in range(len(connections)):
    if i not in visited:
        ans+=dfs(0, i, 0)
print(ans)
graph=[[] for i in range(len(connections))]
print(graph)
for a, b in connections:
        graph[a].append((b, 1))
        graph[b].append((a, 0))


