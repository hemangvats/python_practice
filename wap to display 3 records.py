# Hemang Vats, XI-A, WAP to display three records of books
check=('YES','Yes','YEs','YeS','yes','yES','yeS','yEs','Y','y')
x='yes'
tup=()
l=[]
d={}
while x in check:
    print("""         1. Add Book Record
         2. Delete Book Record
         3. Display Records
         4. Exit""")
    choice=int(input('Enter the number of your choice:'))
    if choice==1:
        Id=input('Enter book id:')
        d['Book_Id']=Id
        name=input('Enter book name:')
        d['Book_Name']=name
        price=float(input('Enter price of the book:'))
        d['Price']=price
        discount=int(input('Enter discount in percentage:'))
        d['Discount']=discount
        tup=tuple(d.values())
        l.append(tup)
        print('The record is added successfully')
        print()
        continue
    elif choice==2:
        y=input('Enter id of the book which you want to delete:')
        for z in l:
            if y in tup:
                del tup
                print('The record is deleted')
                break
        print()
        continue
    elif choice==3:
        print('Book Id','Book Name','Price','Discount',sep='         ')
        for r in l:
            print()
            for num in range(0,4):
                e=r[num]
                print(e,end='         ')
        print()
        continue
    elif choice==4:
        ch=input('Do you want to exit?:')
        if ch in check:
            print('Thank you for using this app')
            print()
            break
        else:
            print('Please enter vaild input')
            print()
            continue
    else:
        print('Please enter vaild input')
        print()
        continue
        
                    
