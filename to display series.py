# Hemang Vats, XI-A, to display series
num=int(input('Enter a number:'))
p=1
r=0
while p<=num:
    product=1
    for x in range(p,1,-1):
        product=product*x
        r=r+p/product
        p+=1
print(r)
y=1
while y<=num:
    y+=1
        

        
                
            
