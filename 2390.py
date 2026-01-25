s = "leet**cod*e"
ans=[]
for i in range(len(s)):
    if s[i]!='*':
        ans.append(s[i])
    else:
        ans.pop()
print(''.join(ans))

