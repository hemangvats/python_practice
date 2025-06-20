# Hemang Vats, XI-A, To displaying the sum of series
num=int(input('Enter a number:'))
x=0
Sum=0
for y in range(1,num+1,2):
    x+=1
    if(x%2==0):
        Sum=Sum+((-1)*(y**2))
        print(-(y**2))
    else:
        Sum=Sum+(y**2)
        print(y**2)
print('Sum=',Sum)
