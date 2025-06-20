# Hemang Vats , XII-A , to display,add,delete and modify the data from a binary file
import pickle
import os
def menu():
    print("""Please select your action
1. ADD
2. MODIFY
3. DELETE
4. DISPLAY
5. EXIT""")
def add():
    f=open('pro6.dat','ab')
    l=[]
    try:
        BId=int(input('Enter your booking id:'))
        l.append(BId)
        Arrival=input('Enter the time for departure:')
        l.append(Arrival)
        Destination= input('Enter your destination:')
        l.append(Destination)
        DOJ=input('Enter the date of departure:')
        l.append(DOJ)
        fare=float(input('Enter the fare for the journey:'))
        l.append(fare)
        pickle.dump(l,f)
    except:
        print('Please enter valid values')
    finally:
        f.close()
def display():
    f=open('pro6.dat','rb')
    try:
        while(f):
            l=pickle.load(f)
            for x in l:
                print(x)
            print()
    except:
        z='File completed'
    finally:
        f.close()
def selective(BId):
    f=open('pro6.dat','rb')
    try:
        while(f):
            l=pickle.load(f)
            if BId in l:
                for x in l:
                    print(x)
                break
            else:
                continue
    except:
        z='File compeleted'
    finally:
        f.close()
def delete(BId):
    f=open('pro6.dat','rb')
    f1=open('temp.dat','wb')
    try:
        while(f):
            l=pickle.load(f)
            if BId in l:
                continue
            else:
                pickle.dump(l,f1)
    except:
        z='File is complete'
    finally:
        f.close()
        f1.close()
        os.remove('pro6.dat')
        os.rename('temp.dat','pro6.dat')
def modify(BId,old):
    f=open('pro6.dat','rb')
    f1=open('temp.dat','wb')
    try:
        while(f):
            l=pickle.load(f)
            if BId in l:
                m=[]
                for x in l:
                    if x==l[(old-1)]:
                        if l[(old-1)]==0:
                            new=int(input('Enter the new value:'))
                        elif l[(old-1)]==4:
                            new=float(input('Enter the new value:'))
                        else:
                            new= input('Enter the new value:')
                        m.append(new)
                    else:
                        m.append(x)
                pickle.dump(m,f1)
            else:
                pickle.dump(l,f1)
    except:
        z='File completed'
    finally:
        f.close()
        f1.close()
        os.remove('pro6.dat')
        os.rename('temp.dat','pro6.dat')
x='yes'
while x=='yes':
    menu()
    no=int(input('Enter your choice by entering the number:'))
    if no==1:
        add()
        print('The data is added')
        continue
    elif no==2:
        try:
            BId=int(input('Enter the booking id for which you need to edit the data:'))
            print("""1. BOOKING ID
2. TIME OF DEPARTURE
3. DESTINATION
4. DATE OF JOURNEY
5. FARE""")
            old=int(input('Enter the number of the data you want to edit:'))
        except:
            x='Enter valid values'
        if (old>5) and (old<1):
            print('Enter valid choice:')
            continue
        else:
            modify(BId,old)
            print('The data is modified')
            continue
    elif no==3:
        try:
            BId=int(input('Enter the booking id for which you need to delete the data:'))
        except:
            x='Enter valid values'
        delete(BId)
        print('The data is deleted')
        continue
    elif no==4:
        print("""1. COMPLETE
2. SELECTIVE""")
        try:
            num=int(input('Enter the number corresponding to your choice:'))
        except:
            x='Enter valid values'
        if num==1:
            display()
        elif num==2:
            BId=int(input('Enter the booking id of the data which you need to display:'))
            selective(BId)
            continue
    elif no==5:
        print('Thank you for joining in')
        break
    else:
        print('Please enter valid number')
        continue
                
                
        
            

                

    
    
    
