class Solution:
    def searchInsert(self,nums: list[int],target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target :
                high=mid-1
            if nums[mid]<target:
                low=mid+1
            if nums[mid]==target:
                return mid
        return low
solution=Solution()
print(solution.searchInsert([1,2,3,4,5,6],4))


