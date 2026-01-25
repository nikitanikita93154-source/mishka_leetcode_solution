nums=[[3,2,1],[1,7,6],[2,7,7]]
ans=0
b={}

for i in range(len(nums)):
    r=tuple([nums[j][i] for j in range(len(nums[i]))])
    if r not in b:
        b[r]=1
    else:
        b[r]+=1
for i in range(len(nums)):
    if tuple(nums[i]) in b:
        ans+=b[tuple(nums[i])]


print(b)
print(ans)
