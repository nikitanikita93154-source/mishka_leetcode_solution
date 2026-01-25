class Solution:
    def findMaxForm(self,strs: list[str],m:int,n:int):
        dp={(0,0):0}
        for s in strs:
            zeroes=s.count('0')
            ones=s.count('1')
            newdp={}
            for (ZEROES,ONES),val in dp.items():
                newZEROES,newONES=ZEROES+zeroes,ONES+ones
                if newONES<=m and newONES<=n:
                    newdp[(newZEROES,newONES)]=val+1
            dp.update(newdp)
            return max(dp.values())
solution=Solution()
print(solution.findMaxForm(['10','0001','111001','1','0'],5,3))


