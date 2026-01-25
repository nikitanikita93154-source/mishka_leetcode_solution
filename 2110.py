nums=[12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7]
j=0
i=1
ans=0
while i<len(nums):
    if nums[i-1]-nums[i]==1:
        i+=1
    elif nums[i-1]==nums[i]:
        ans+=1
        j=i
        i+=1
    else:

        ans += (i-j)*((i-j+1)//2)
        print((i-j),i-j+1)
        print((i-j)*((i-j+1)//2))
        j=i
        i+=1
print(j,i)
print(ans+(i-j)*((i-j+1)//2))
count = 1
