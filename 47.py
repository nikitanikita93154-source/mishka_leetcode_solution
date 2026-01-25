a=[1,1,3]
ans=[]
def recurs(used,p):
    if len(p)==len(a):
        ans.append(p.copy())
        return
    for i in range(len(a)):
        if i not in used:
            used.append(i)
            p.append(a[i])
            recurs(used,p)
            p.pop()
            used.pop()
recurs([],[])
ans= [list(item) for item in set(tuple(sublist) for sublist in ans)]
print(ans)
