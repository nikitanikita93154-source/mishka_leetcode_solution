


class Solution:
    def addBinary(self,a:str,b:str)->str:
        a_10=int(a,2)
        b_10 = int(b, 2)
        c=bin(a_10+b_10)
        return c[2:]
solution=Solution()
print(solution.addBinary('11','1'))