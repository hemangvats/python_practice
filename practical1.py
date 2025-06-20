# Hemang vats, XII-A, To create a stack and also pop all the data from the stack
d={}
s=[]
def dictionary():
    global d
    num=int(input('Enter the number of records you want to enter:'))
    for x in range(0,num):
        name=input('Enter name of item:')
        price=int(input('Enter price of the item:'))
        d[name]=price
    print(d)
def push ():
    global d
    global s
    l=d.keys()
    for x in l:
        if d[x]>25:
            s.append(x)
        else:
            continue
    print(s)
def pop():
    global s
    m=len(s)
    for n in (0,m):
        if m>0:
            break
        else:
            x=s.pop()
            print(x)
dictionary()
push()
pop()
    
    
