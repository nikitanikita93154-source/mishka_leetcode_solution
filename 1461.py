s='00110'
k=2
n=2**k
v={}
i=ans=0
while i+k<=len(s):
    if s[i:i+k] not in v:
        v[s[i:i+k]]=1
        ans+=1
    i+=1
print(v)
print(ans==n)
