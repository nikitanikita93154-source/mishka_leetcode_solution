nums=[4]
k=3
if len(nums)==1 and k==nums[0]:
    print(1)
nums.sort()
i=ans=0
j=len(nums)-1
while i<j:
    if nums[i]+nums[j]<k:
        i+=1
    elif nums[i]+nums[j]>k:
        j-=1
    else:
        ans+=1
        i+=1
        j-=1
print(ans)
