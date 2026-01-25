s='aaaaAaaa'
s1=sorted(s)
print(s1)
a=[]
index=0
flag=0
res=0
for i in range(len(s1)-1):
    index+=1
    if s1[i]!=s1[i+1]:
        if i%2!=0 and flag==0:
            res+=index
            flag=1
        elif i%2==0:
            res+=index
        else:
            res+=index
        index=0
if flag==1:
    print(res+1)
else:
    print(res+1)