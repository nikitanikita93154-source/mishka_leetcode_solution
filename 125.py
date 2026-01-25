class Solution:
    def isPalinom(self,s:str)-> bool:
        s2=''
        for i in s.lower():
            if i in 'qwertyuiopasdfghjklzxcvbnm0123456789':
                s2+=i
        p1=s2
        p2=s2[::-1]
        n=len(s2)//2
        if p1[:n]==p2[:n]:
            return True
        else:
            return False
solution=Solution()
print(solution.isPalinom('0P'))