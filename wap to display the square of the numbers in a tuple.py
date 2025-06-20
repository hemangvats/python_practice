# Hemang Vats, XI-A, WAP to display the square of the numbers from a tuple
l=[]
for x in range(0,3):
    num1=int(input('Enter a number:'))
    l.append(num1)
tup1=tuple(l)
for x in tup1:
    print(x**2)
