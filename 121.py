class Solution:
    def maxProfit(self,prices:list[int])->int :
        manx=prices[0]
        minx = prices[0]
        ans=0
        for i in  prices:
            if i<minx:
                minx=i
                manx=i
            if i>manx:
                manx=i
            if ans<manx-minx:
                ans=manx-minx
        return ans
solution=Solution()
print(solution.maxProfit([2,4,1]))
