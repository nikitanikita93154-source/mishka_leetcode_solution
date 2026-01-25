nums = [5,2,2,2]
nums.sort()
nums0=[i for i in nums if i%3==0]
nums1=[i for i in nums if i%3==1]
nums2=[i for i in nums if i%3==2]
print(nums0,nums1,nums2)
num = sum(nums0) + sum(nums1) + sum(nums2)
if num % 3 == 0:
    print(sum(nums))
elif num % 3 == 1:
    if len(nums2) >= 2 and len(nums1)>=1 and nums1[0] <= (nums2[0] + nums2[1]):
        print(num - nums1[0])
    elif len(nums2) >= 2 and len(nums1)>=1 and nums1[0] > (nums2[0] + nums2[1]):
        print(num-(nums2[0] + nums2[1]))
    elif len(nums2) < 2 and len(nums1)>=1:
        print(num - nums1[0])
    elif len(nums2) > 2 and len(nums1)<1:
        print(num -(nums2[0] + nums2[1]))
    else:
        print(sum(nums0))
elif num % 3 == 2:
    if len(nums1) >= 2 and len(nums2)>=1 and  nums2[0] <= (nums1[0] + nums1[1]):
        print(num - nums2[0])
    elif len(nums1) >= 2 and len(nums2)>=1 and nums2[0] > (nums1[0] + nums1[1]):
        print(num-(nums1[0] + nums1[1]))
    elif len(nums1) < 2 and len(nums2)>=1:
        print(num - nums2[0])
    elif len(nums1) > 2 and len(nums2)<1:
        print(num -(nums1[0] + nums1[1]))
    else:
        print(nums0)


