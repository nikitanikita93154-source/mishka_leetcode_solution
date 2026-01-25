
class Solution:
    def marge(self,nums1:list[int],m:int,nums2:list[int],n:int)->list:
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        return nums1
solution=Solution()
print(solution.marge([1,2,3,0,0,0],3,[2,5,6],3))