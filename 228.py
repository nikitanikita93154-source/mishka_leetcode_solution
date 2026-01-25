class Solution:
    def summaryRanges(self,nums:list[int])->list[str]:
        a=[]
        start = nums[0]
        for i in range(len(nums)-1):

            if nums[i]!=nums[i+1]-1:
                if start!=nums[i]:
                    a.append(f'{start}->{nums[i]}')
                    start=nums[i+1]
                else:
                    a.append(f'{start}')
                    start = nums[i + 1]
        if start!=nums[-1]:
            a.append(f'{start}->{nums[-1]}')
        else:
            a.append(f'{nums[-1]}')
        return a
solution=Solution()
print(solution.summaryRanges([0,2,3,4,6,8,9]))
