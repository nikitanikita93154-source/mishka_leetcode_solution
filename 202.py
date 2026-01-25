class Solution:
    def  isHappy(self,n:int)-> bool:
        n=str(n)
        ones = []
        while True:
            one=0
            for i in n:
                one+=int(i)**2
            if one==1:
                return True
            elif one not in ones :
                ones.append(one)
                n=str(one)
            else:
                return False

solution=Solution()
print(solution.isHappy(2))