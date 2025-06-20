# Hemang Vats, XI-A, WAP to display item name and profit or loss
check=('YES','Yes','YEs','YeS','yes','yES','yeS','yEs','Y','y')
x='yes'
d={}
while x in check:
    item=input('Enter item name:')
    d['Item_Name']=item
    cp=float(input('Enter the cost price:'))
    d['CP']=cp
    sp=float(input('Enter selling price:'))
    d['SP']=sp
    print('Item_Name',':',d['Item_Name'])
    if d['SP']>d['CP']:
        profit=d['SP']-d['CP']
        print('Profit=',profit)
    else:
        loss=d['CP']-d['SP']
        print('Loss=',loss)
    x=input('Do you want to continue?')
    if x in check:
        continue
    else:
        break
