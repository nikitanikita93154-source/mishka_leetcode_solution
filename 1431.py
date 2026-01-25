candies=[2,3,5,1,3]
extraCandies=3
ans=[i+extraCandies>=max(candies) for i in candies]
print(ans)