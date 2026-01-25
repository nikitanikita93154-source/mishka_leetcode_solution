class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        left = [set()]
        comb = set()
        for i in range(n):
            left.append(left[-1] | {s[i]})
        right = [set()]
        for i in range(n - 1, -1, -1):
            right.append(right[-1] | {s[i]})
        right = right[::-1]
        for k in range(1, n - 1):
            y = s[k]
            com = left[k] & right[k+1]
            for i in com:
                comb.add(i + y + i)
        return len(comb)
solution=Solution()
print(solution.countPalindromicSubsequence('ckafnafqo'))
s = "ckafnafqo"
n = len(s)
comb=set(s)
res=0
for i in comb:
    left=s.find(i)
    right=s.rfind(i)
    print(left,right)
    if left!=right:
        res+=len(s(set([left+1:right])
print(res)