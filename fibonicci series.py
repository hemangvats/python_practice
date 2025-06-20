# Hemang Vats , XI-A , to display the pattern
check='yes'
while check=='yes':
    if check=='yes':
        num=int(input('Enter a number:'))
        x=0
        y=1
        print(x)
        print(y)
        for z in range(num):
            if z<=1:
                b=z
            else:
                b=x+y
                x=y
                y=b
                print(b)
        check=input('Do you want to continue? yes or no?:')
        continue
    else:
        break

    
        
