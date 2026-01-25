nums=[1,1,5]
ans=[]
def recurs(n,u):
    if len(n)==len(nums):
        ans.append(n.copy())
        return n
    for i in range(len(nums)):
        if i not in u:
            u.append(i)
            print(u)
            n+=[nums[i]]
            recurs(n,u)
            n.pop()
            u.pop()
recurs([],[])
print(ans)
