class Solution:
    def plusOne(self,digits:list[int])->list[int]:
        num=''
        for i in digits:
            num+=str(i)
        ans_num=int(num)+1
        numbers=[int(i) for i in str(ans_num)]
        return numbers
solution=Solution()
print(solution.plusOne([1,1,1]))