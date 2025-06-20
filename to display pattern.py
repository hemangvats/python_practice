#Hemang Vats ,XI-A , to display a number in a pattern
check='yes'
while check=='yes':
    if check=='yes':
        num=int(input('Enter a number:'))
        if num<=0:
            print('Enter a valid number')
        else:
            num1=0
            for x in range(1,num+1,1):
                num1=num1*10+x
                print(num1)
        check=input('Do you want to continue? yes or no?:')
        continue
    else:
        break

