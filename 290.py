class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = {}
        s=s.split()
        for i in range(len(pattern)):
            if pattern[i] in a :
                if a[pattern[i]]==s[i]:
                    continue
                else:
                    print(a)
                    return False
            else:
                a[pattern[i]]=s[i]
        return len(a) == len(set(a.values()))

solution=Solution()
print(solution.wordPattern("abba", "dog cat cat dog"))