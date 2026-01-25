s="__the______"
ans=[]
w=''
s+=' '
for i in range(len(s)):
    if s[i]!="_":
        w+=s[i]
    elif s[i]=="_" and w!='':
        ans.append(w)
        w=''
ans=ans[::-1]
a='_'.join(ans)
print(a)
