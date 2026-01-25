class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        index=0
        for i in nums:
            if i%3!=0:
                index+=1
        return index
solution=Solution()
print(solution.minimumOperations([1,2,3,4,1231231,11,1,1,1,1,1,2,3,4,5]))
print(26%3)