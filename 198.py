nums=[1]
new_nums=nums.copy()
for i in range(len(nums)):
    for j in range(i+2,len(nums)):
        new_nums[j]=max(new_nums[j],(nums[j]+new_nums[i]))
print(max(new_nums))