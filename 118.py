class Solution:
    def generate(self,numrows: int)-> list[list[int]]:
        l2=[[1]]
        index=1
        for i in range(1,numrows):
            l=[1]
            for j in range(1,index):
                l.append(l2[i-1][j-1]+l2[i-1][j])
            l.append(1)
            index+=1
            l2.append(l)
        return l2
solution=Solution()
print(solution.generate(5))