# Hemang Vats, XII-A, WAP to calculate simple interest using try and except block
def test():
    try:
        principle=int(input('Enter the principle amount:'))
        rate=float(input('Enter the rate of interest:'))
        time=float(input('Enter the time:'))
        interest=(principle*rate*time)/100
        print()
        print('The interest will be',interest)
        amount=principle+interest
        print()
        print('The total payable amount after',time,'years is',amount)
    except:
        return('Please enter valid values')
x=test()
if x=='Please enter valid values':
    while x=='Please enter valid values':
        print()
        print('Please enter values again')
        print()
        x=test()
else:
    print()
    y=input('Do you wish to continue?:')
    if y in ('yes','Yes','y','Y','YES','YeS','YEs','yES','yeS'):
        while y in('yes','Yes','y','Y','YES','YeS','YEs','yES','yeS'):
            print()
            x=test()
                
        
   
    
