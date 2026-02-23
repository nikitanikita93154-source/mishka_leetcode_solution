s='Aabb'
k={}
for si in s:
    if si in k:
        k[si]+=1
    else:
        k[si]=1
ans= sorted( k, key=k.get, reverse=True)
a=''
for i in ans:
   a+=i*k[i]
print(a)
