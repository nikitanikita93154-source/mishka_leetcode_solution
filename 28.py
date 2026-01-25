class Solution:
    def strStr(self,haystack:str,needle:str) -> int:
        num=len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+num]==needle:
                return i
        return -1
solutino=Solution()
print(solutino.strStr('aaasadbutsac','sad'))