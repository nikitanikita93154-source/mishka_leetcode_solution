
class Solution:
    def mySqrt(self,x:int)-> int:
        if x==0:
            return 0
        x_n=0.5*(x/2+x/(x/2))
        x_n2=0
        while True:
            x_n2=0.5*(x_n+x/(x_n))
            if abs(x_n2-x_n)<0.1:
                return int(x_n2)
            x_n=x_n2
solution=Solution()
print(solution.mySqrt(144))