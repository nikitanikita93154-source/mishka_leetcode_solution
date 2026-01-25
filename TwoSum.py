class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for n in range(i+1,len(nums)):
                if nums[i]+nums[n]==target:
                    return [i,n]
        return []

nums = [2, 5, 5, 7]
target = 10
solution = Solution()
print(solution.twoSum(nums, target))