nums=[2,1]
nums1=list(set(nums))
nums1.sort()
if len(nums1)==1:
    return nums[0]
if len(nums1)<3:
    print(nums1[-3+len(nums)])
else:
    print(nums1[-3])