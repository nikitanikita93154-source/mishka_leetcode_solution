class Solution:
    def lenghtOfLastWorld(self,s:str)->int:
        st=s[::-1]
        a=0
        for i in range(len(st)):
            if st[i]!=' ':
                a+=1
            if st[i]==' ' and a!=0:
                return int(a)
        return a

solution = Solution()
print(solution.lenghtOfLastWorld('                 Hello                 World    '))