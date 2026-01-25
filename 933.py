class RecentCounter:

    def __init__(self):
        self.requests=[]
        self.ans=0
    def ping(self, t: int) -> int:
        self.requests.append(t)
        print(self.requests)
        while self.requests[self.ans]< t-3000:
            print(self.requests[self.ans])
            self.ans+=1
        return len(self.requests)-self.ans
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)

print(param_1,param_2,param_3,param_4)