#Hemang Vats, if a number is palindrome or not
check='yes'
while check=='yes':
    if check=='yes':
        num=int(input('Enter a number:'))
        num1=num
        num2=0
        while num>0:
            num3=num%10
            num2=num2*10+num3
            num=num//10
        if num1==num2:
            print('It is a palindrome')
        else:
            print('It is not a palindrome')
        check=input('Do you want to continue? yes or no?:')
        continue
    if(check!='yes'):
        break
    
