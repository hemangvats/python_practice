# Hemang Vats, XI-A, WAP to display the largest and the smallest no
l=[]
for x in range(0,10):
    num=int(input('Enter a number:'))
    l.append(num)
tup1=tuple(l)
y=max(tup1)
z=min(tup1)
print(y,'is the maximum number you entered')
print(z,'is the minimum number you entered')
