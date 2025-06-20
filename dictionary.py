# Hemang Vats, XI-A, WAP to accept things in a dictionary
d={}
check='yes'
while check=='yes':
    if check=='yes':
        name=input('Enter item name:')
        d['Item_name']=name
        cp=int(input("Enter cost price:"))
        d['Cost_price']=cp
        sp=int(input('Enter selling price:'))
        d['Selling_price']=sp
        if d['Selling_price']> d['Cost_price']:
            x=d['Selling_price']-d['Cost_price']
            print('Profit',x,sep='=')
        elif d['Cost_price']>d['Selling_price']:
            x=d['Cost_price']-['Selling_price']
            print('Loss',x,sep='=')
        else:
            print('No profit nor loss')
        check=input('Do you want to continue? yes or no?:')
        continue
    if(check!='yes'):
        break
