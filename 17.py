class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digits=[int(i) for i in digits ]
        deep=0
        ans=[]
        flag=len(digits)
        a=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

        def recurs(deep, current):
            if deep ==flag:
                ans.append(current)
                return
            for i in a[digits[deep] - 2]:
                recurs(deep + 1, current + f'{i}')
        recurs(deep,'')
        ans.sort()
        return ans
solution=Solution()
print(solution.letterCombinations('23'))
ans=[]
a=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

def recurs(deep, current):
    digit=[2,3]
    if deep == -1:
        ans.append(current)
        print(ans)
        return
    for i in a[digit[deep]-2]:
        recurs(deep - 1, current +f'{i}')

#print(ans)
#print(recurs(1, ''))