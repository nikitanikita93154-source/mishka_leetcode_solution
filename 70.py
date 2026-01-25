import  math
class Solution:
    def climbStairs(self,n:int)->int:
        index=0
        for i in range(0,(n//2)+1):
            index+=math.factorial(n-i)/(math.factorial(i)*math.factorial(n-i*2))
        return int(index)
solution=Solution()
print(solution.climbStairs(2))