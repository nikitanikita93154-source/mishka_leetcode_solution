class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans=10000000000
        p=0
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:
                tr=nums[i]+nums[j]+nums[k]
                print('tr',tr)
                print('target-tr',abs(target-tr))
                if tr<target:
                    j+=1
                    if ans>abs(target-tr):
                        ans=abs(target-tr)
                        p=tr
                elif tr>target:
                    k-=1
                    if ans>abs(target-tr):
                        ans=abs(target-tr)
                        p=tr
                else:
                    return target
        print(p)
        print(ans)

solution=Solution()
print(solution.threeSumClosest([-1,2,1,-4],1))