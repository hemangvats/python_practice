# Hemang Vats, XI-A, program to display even multiple of a number till 50
num=int(input('Enter a number:'))
x=1
product=num*x
while(product<50):
    if (product%2==0):
        print(product)
    x=x+1
    product=num*x
        


