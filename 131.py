s='aaab'
bigans=[]
def recurs(ans,s):
    print(ans,s)
    if len(s)==1:
        ans.append(s)
        bigans.append(ans)
        return
    for i in range(1,len(s)+1):
        if s[:i]==s[:i][::-1]:

ans=recurs([],s)
print(bigans)