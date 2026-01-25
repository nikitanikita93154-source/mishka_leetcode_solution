class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums.sort()

        i=original
        for index in range(len(nums)):
            if nums[index]==i:
                i*=2
        return i
solution=Solution()
print(solution.findFinalValue([5,3,6,1,12],4))
