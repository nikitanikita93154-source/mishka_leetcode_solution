x=y=6
n=5000
for i in range(2,n+1):
    new_x=(3*x+2*y)%1000000007
    new_y = (2 * x + 2 * y)%1000000007
    x,y=new_x,new_y
print((x+y)%1000000007)