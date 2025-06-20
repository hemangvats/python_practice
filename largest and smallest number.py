#Hemang Vats, XI-A, Largest and samllest number
num=int(input('Enter a number'))
count=1
largest=0
num1=num
num2=num
while count<=9:
    count+=1
    num3=int(input('Enter a number'))
    num4=num3
    num5=num3
    if num3>num:
        largest=num3
        smallest=num
    elif num>num3:
        largest=num
        smallest=num3
print('Largest number is',largest)
