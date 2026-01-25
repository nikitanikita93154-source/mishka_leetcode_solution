matrix = [[2,9,3],[5,4,-4],[1,7,1]]
m=float('-inf')
ans=index=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]>0:
            ans+=matrix[i][j]
            m = max(m, -matrix[i][j])
        elif matrix[i][j]<1:
            ans-=matrix[i][j]
            m=max(m,matrix[i][j])
            index+=1
print(ans,m,index)
if index%2!=0:
    ans+=m*2
print(ans)
