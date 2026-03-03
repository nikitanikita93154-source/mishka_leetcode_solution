nums=[4,4,3,2,1]
visited=set()
ans=[]
def backtrack(a,i):
    if len(a)>=2 and tuple(a) not in visited:
        ans.append(a)
        visited.add(tuple(a))
    for x in range(i,len(nums)):
        if not a:
            a.append(nums[x])
        elif a and a[-1]<=nums[x]:
            a.append(nums[x])
            backtrack(a.copy(),x+1)
            a.pop()
for i in range(len(nums)):
    backtrack([],i)
print(ans)