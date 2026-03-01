s="101023"
ans=[]
def backtrack(a,i):
    if len(a)==4 and i==len(s):
        ans.append(a)
        return
    if i==len(s):
        return
    if not a:
        a.append(s[i])
        backtrack(a.copy(),i+1)
        return
    if a[-1]=='0':
        a.append(s[i])
        backtrack(a.copy(), i + 1)
        return
    if len(a[-1]) < 4 and int(a[-1] + s[i]) < 256:
        a[-1] = a[-1] + s[i]
        backtrack(a.copy(), i+1)
        a[-1] = a[-1][:-1]
    if len(a)<4:
        a.append(s[i])
        backtrack(a.copy(),i+1)
backtrack([],0)
an=[]
for i in ans:
    an.append('.'.join(i))
print(an)


