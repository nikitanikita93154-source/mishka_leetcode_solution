word1='cabbba'
word2='abbccd'
a=[0]*26
b=[0]*26
for i in word1:
    n=ord(i)-ord('a')
    a[n]+=1
for i in word2:
    n=ord(i)-ord('a')
    b[n]+=1
for i in range(26):
    if (b[i]==0 and a[i]!=0) or (b[i]!=0 and a[i]==0):
        print('no')
print(a)
print(b)
a.sort()
b.sort()
for i in range(26):
    if b[i]!=a[i]:
        print('no')





