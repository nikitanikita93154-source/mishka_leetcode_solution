nums=[5,1,5,2,5,3,5,4]
d={}
for i in nums:
    if i in d:
        print(i)
    d[i] = 1
