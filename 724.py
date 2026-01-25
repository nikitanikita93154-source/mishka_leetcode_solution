nums=[-1,-1,-1,-1,-1,-1]
total=sum(nums)
left=0
for i in range(len(nums)):
    print(total,left)
    if total-nums[i]==left:
        print(i)
        break
    total-=nums[i]
    left+=nums[i]
print(-1)

