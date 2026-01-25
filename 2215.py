a=[1,1,2,2,3]
b={}
for i in (range(len(a))):
    if a[i] not in b:
        b[a[i]]=1
    else:
        b[a[i]] += 1
print(len(b.values()))
print(len(set(b.values())))
