nums=[1,4,4,4]
visit=set()
ans=[[]]
def backtrack(a,num):
    for i in range(len(num)):
        a.append(num[i])
        new_a=a.copy()
        new_a.sort()
        if tuple(new_a) not in visit:
            ans.append(new_a.copy())
            visit.add(tuple(new_a))
            new_num=num.copy()
            new_num.pop(i)
            backtrack(new_a.copy(),new_num)
        a.pop()
backtrack([],nums)
print(ans)
