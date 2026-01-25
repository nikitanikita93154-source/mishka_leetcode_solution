

class Solution:
    def reverseBits(self, n:int)->int:
        if not n:
            return 0
        n='0'*(32-len(str(bin(n)[2:])))+bin(n)[2:]

        return int(n[::-1],2)

solution=Solution()
print(solution.reverseBits(43261596))