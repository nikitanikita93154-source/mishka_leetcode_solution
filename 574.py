# isC = [[1,0,0],[0,1,0],[0,0,1]]
#
# q=[0]
# num=set()
# num.add(0)
# while q:
#     for i in range(len(isC)):
#         if isC[q[0]][i]==1 and i not in num:
#             q.append(i)
#             print(q)
#             num.add(i)
#     q.pop(0)
# print(num)
# ans=1
# for i in range(len(isC)):
#     q=[i]
#     if i not in num:
#         while q:
#             for j in range(len(isC)):
#                 if isC[q[0]][j] == 1 and j not in num:
#                     q.append(j)
#                     print(q)
#                     num.add(j)
#             q.pop(0)
#         ans+=1
# print(num)
# print(ans)
visited = set()
isC = [[1,1,0],[1,1,0],[0,0,1]]
ans=0
def dfs(node):
    visited.add(node)
    for neighbor in range(len(isC[node])):
        if isC[node][neighbor]==1 and neighbor not in visited:
            dfs(neighbor)

for i in range(len(isC)):
    if i not in visited:
        dfs(i)
        ans+=1
print(ans)
print(visited)

