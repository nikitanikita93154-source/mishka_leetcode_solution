class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        index=0
        for i in range(len(nums)):
            if nums[i]==1 and index:
                index=0
            elif nums[i]==0:
                index+=1
            else:
                return False
        return True
solution=Solution()
print(solution.kLengthApart([1,0,0,1,0,1],2))

