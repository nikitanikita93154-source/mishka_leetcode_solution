# heights = [2,4,4,6]
# stack=[]
# max_pl=0
# heights.append(0)
# for i,h in enumerate(heights):
#     while stack and heights[stack[-1]]>h:
#         height=heights[stack.pop()]
#         if  not stack:
#             width=i
#         else:
#             width=i-stack[-1]-1
#         max_pl=max(max_pl,height*width)
#     stack.append(i)
# print(max_pl)
import multiprocessing
digits=[1,2,9]
digits.reverse()
ans=''
flag = 1
for i in range(len(digits)):
    if flag == 1:
        if digits[i] + 1 >= 10 and i==len(digits)-1:
            ans += '01'
        elif digits[i] + 1 >= 10:
            ans += '0'
        else:
            ans += str(digits[i] + 1)
            flag = 0
    else:
        ans += str(digits[i])
print(ans)
a = []
for i in ans[::-1]:
    a.append(int(i))
print(a)
# nums=[0,1,2,3,4,5,6,7,8,9]
# flag=0
# # if len(nums)<3:
# #     return False
# for i in range(1,len(nums)-1):
#     print(nums[i-1],nums[i],nums[i+1],flag)
#     if flag==0:
#         if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
#             flag=1
#             continue
#         elif nums[i-1]>=nums[i] or nums[i]>=nums[i+1] :
#             print(nums[i])
#             print(1, 'False')
#             break
#     if flag==1:
#         if nums[i-1]>nums[i]>nums[i+1]:
#             continue
#         else:
#             print(2, 'False')
#             break
# if flag==0:
#
# print('True')
