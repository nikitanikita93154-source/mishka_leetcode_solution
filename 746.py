cost=[0,1,2,1]
new_cost=[-1]*len(cost)
new_cost[0]=cost[0]
new_cost[1]=cost[1]
for i in range(2,len(cost)):
    new_cost[i]=cost[i]+min(new_cost[i-1],new_cost[i-2])
print(min(new_cost[-1],new_cost[-2]))
