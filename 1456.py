s='ibpbhixfiouhdljnjfflpapptrxgcomvnb'
k=33
index=0
print(len('ibpbhixfiouhdljnjfflpapptrxgcomvnb'))
for i in s[:k]:
    if i in 'aeiou':
        index+=1
print(index)
m=index
for i in range(k,len(s)):
    if s[i-k] in 'aeiou':
        index-=1
    if s[i] in 'aeiou':
        index+=1
    if index>m:
        m=index
print(m)

