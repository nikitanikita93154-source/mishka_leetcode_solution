n=45
k=9
ans_end=[]
def recurs(deep,num,ans,ni):
    print(ans)
    if deep==k and num==n:
        print(ans)
        ans_end.append(ans)
        return ans
    for i in range(ni,9):
        ans.append(i)
        recurs(deep+1,num+i,ans.copy(),i+1)
        ans.pop()
recurs(0,0,[],1)
print(ans_end)


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans_end = []

        def recurs(deep, num, ans, ni):
            if deep == k and num == n:
                print(ans)
                ans_end.append(ans)
                return ans
            for i in range(ni, 10):
                ans.append(i)
                recurs(deep + 1, num + i, ans.copy(), i + 1)
                ans.pop()


        recurs(0, 0, [], 1)
        print(ans_end)
        return ans_end
solution=Solution()
print(solution.combinationSum3(9,45))