# nums=[1,2,3,4,3]
# stack=[]
# n=[-1]*len(nums)
# for i in range(len(nums)):
#     while stack and nums[i]>nums[stack[-1]]:
#         num=stack.pop()
#         n[num]=nums[i]
#     stack.append(i)
# for i in range(len(nums)):
#     while stack and nums[i]>nums[stack[-1]]:
#         num=stack.pop()
#         n[num]=nums[i]
#     stack.append(i)
# print(n)
s = "cbacdcbc"
stack=[]
b_s={}
vis_stack=set()
for i in range(len(s)):
    b_s[s[i]]=i+1
for i,char in enumerate(s):
    if char in vis_stack:
        continue
    while stack and char<stack[-1] and i<b_s[stack[-1]]:
        vis_stack.remove(stack.pop())
    stack.append(char)
    vis_stack.add(char)
print(stack)