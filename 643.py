nums=[1,12,-5,-6,50,3]
k=4
s=sum(nums[:4])/k
m=s
for i in range(k,len(nums)):
    s = sum(nums[:i]) - sum(nums[:i - k])
    if m<s/k:
        m=s/k
return round()
