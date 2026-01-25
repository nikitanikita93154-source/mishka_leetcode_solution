s='qwerty'
t='qwertyt'
a=sorted(s)
b=sorted(t)
i=j=0
while i<len(a) and j<len(b):
    if a[i]!=b[j]:
        print(b[j])

    j+=1
    i+=1