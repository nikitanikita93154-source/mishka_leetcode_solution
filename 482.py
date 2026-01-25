s='5F3-Z-2E-9-W'
k=1
s=s.replace('-','')
n=len(s)
first=n%k or k
res=s[:first]
print(first,len(s),k)
for i in range(first,len(s),k):
    res += '-'
    res+=s[i:k+i].upper()
print(res)
