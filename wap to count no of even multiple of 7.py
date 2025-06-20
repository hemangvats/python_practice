# Hemang Vats, XI-A, WAP to count the number of even multiple of 7
l=[]
count=0
for x in range(0,10):
    num=int(input('Enter the number:'))
    l.append(num)
for y in l:
    if y==0:
        continue
    if y%14==0:
        count+=1
    else:
        continue
if count==0:
    print('No number is a even multiple of 7 from the numbers you have entered')
else:
    print('The number of even multiple of 7 are',count)
    
