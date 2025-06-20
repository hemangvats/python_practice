# Hemang Vats, XI-A, printing the series
y=int(input('Enter terminating point:'))
print(1)
for x in range(1,y+1,1):
    if((x/5)%2==1):
        a=x*(-1)
        print(a)
    elif((x/5)%2==0):
        print(x)
    
