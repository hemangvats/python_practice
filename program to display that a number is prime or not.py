#Hemang Vats, XI-A, to check wether the number is prime or not
check='yes'
while check=='yes':
    if check=='yes':
        num=int(input('Enter a number:'))
        if num==2:
            print('Prime number')
        elif num<1:
            print('Enter valid number')
        elif num==1:
            print('Not a prime number')
        else:
            for x in range(2,num):
                if num%x==0:
                    print('Not a prime number')
                    break
            else:
                print('Prime number')
        check=input('Do you want to continue? yes or no?:')
        continue
    if(check!='yes'):
        break
    
    
    
