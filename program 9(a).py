# Hemang Vats , XII-A , to display,add,delete and modify the data from a csv file using dictionary
import csv
import os
def menu():
    print("""Please select your action
1. ADD
2. MODIFY
3. DELETE
4. DISPLAY
5. EXIT""")
def add():
    f=open('data3.csv','a',newline='')
    try:
        code=int(input('Enter the code:'))
        name=input('Enter name:')
        d={code:name}
        c=csv.DictWriter(f,d.keys())
        c.writeheader(code)
        c.writerow(d)
    except:
        print('Enter valid values')
    finally:
        f.close()
def display():
    f=open('data3.csv','r',newline='')
    r=csv.DictReader(f)
    for x in r:
        y=x.values()
        z=x.keys()
        for m in z:
            print(m)
        for n in y:
            print(n)
    f.close()
def selective(pid):
    f=open('data3.csv','r',newline='')
    r=csv.DictReader(f)
    for x in r:
        y=x.values()
        z=x.keys()
        if pid in z:
            for m in z:
                print(m)
            for n in y:
                print(n)
        else:
            continue
    f.close()
def delete(pid):
    f=open('data3.csv','r',newline='')
    f1=open('temp4.csv','w',newline='')
    r=csv.DictReader(f)
    c=csv.DictWriter(f1)
    for x in r:
        y=x.values()
        z=x.keys()
        if pid in z:
            continue
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('data3.csv')
    os.rename('temp4.csv','data3.csv')
def modify(pid,old):
    f=open('data3.csv','r',newline='')
    f1=open('temp4.csv','w',newline='')
    r=csv.DictReader(f)
    c=csv.DictWriter(f1)
    for x in r:
        y=x.values()
        z=x.keys()
        if pid in z:
            if old=='code':
                new=input('Enter the new code:')
                for n in y:
                    d={new:n}
                    c.writerow(d)
            else:
                new= input('Enter the new name:')
                for m in z:
                    d={m:new}
                    c.writerow(d)
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('data3.csv')
    os.rename('temp4.csv','data3.csv')
y='yes'
while y=='yes':
    menu()
    no=int(input('Enter your choice by entering the number:'))
    if no==1:
        add()
        print('The data is added')
        continue
    elif no==2:
        try:
            pid=input('Enter the code of the person whose data you want to modify:')
            old=input('Enter your choice which you want to modify:')
        except:
            x='Enter valid values'
        if (old=='code')or(old=='name'):
            modify(pid,old)
            continue
        else:
            print('Enter valid choice')
            continue
    elif no==3:
        try:
            pid=input("Enter the code of the person whose data you want to delete:")
        except:
            x='Enter valid values'
        delete(pid)
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
            continue
        elif num==2:
            pid=input("Enter the code of the person whose data you want to display:")
            selective(pid)
            continue
        else:
            print('Enter vaild choice')
            continue
    elif no==5:
        print('Thank you for joining in')
        break
    else:
        print('Please enter valid number')
        continue
    
        
    
    
            
        
    
            
        
    
        
    
        
    
