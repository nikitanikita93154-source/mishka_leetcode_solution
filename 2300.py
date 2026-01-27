s=[1231]
d=[1]
d.sort()
n=6
ans=[]
for i in s:
    left,right=0,len(d)-1
    while left<right:
        mid=(left+right)//2
        if d[mid]*i<n:
            left=mid+1
        else:
            right=mid
    if left<len(d) and d[left]*i>=n:
        ans.append(len(d)-left)
    else:
        ans.append(0)
print(ans)