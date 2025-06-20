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
    f=open('data1.csv','a',newline='')
    try:
        Id=int(input('Enter patient id:'))
        name=input("Enter patient's name:")
        dot=input('Enter date of test:')
        result=input('Enter result of RTPCR test:')
        d={'id':Id,'n':name,'d':dot,'r':result}
        c=csv.DictWriter(f,d.keys())
        e={'id':'Id','n':'name','d':'dot','r':'result'}
        c.writerow(e)
        c.writerow(d)
    except:
        print('Enter valid values')
    finally:
        f.close()
def display():
    f=open('data1.csv','r',newline='')
    r=csv.DictReader(f)
    for x in r:
        y=x.values()
        for z in y:
            if z in ['Id','name','dot','result']:
                continue
            else:
                print(z)
    f.close()
def selective(pid):
    f=open('data1.csv','r',newline='')
    r=csv.DictReader(f)
    for x in r:
        if x['Id']==pid:
            y=x.values()
            for z in y:
                print(z)
        else:
            continue
    f.close()
def delete(pid):
    f=open('data1.csv','r',newline='')
    f1=open('temp3.csv','w',newline='')
    r=csv.DictReader(f)
    e={'id':'Id','n':'name','d':'dot','r':'result'}
    c=csv.DictWriter(f1,e)
    c.writerow(e)
    for x in r:
        print(x)
        if x['Id']==pid:
            continue
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('data1.csv')
    os.rename('temp3.csv','data1.csv')
def modify(pid,old):
    d={None}
    f=open('data1.csv','r',newline='')
    f1=open('temp3.csv','w',newline='')
    r=csv.DictReader(f)
    c=csv.DictWriter(f1,d)
    e={'id':'Id','n':'name','d':'dot','r':'result'}
    c.writerow(e)
    for x in r:
        if x['Id']==pid:
            if old==2:
                name=input("Enter new patient's name:")
                x['name']=name
            elif old==3:
                dot=input('Enter new date of test:')
                x['dot']=dot
            else:
                result=input('Enter new result of RTPCR test:')
                x['result']=result
            c.writerow(x)
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('data1.csv')
    os.rename('temp3.csv','data1.csv')
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
            pid=input('Enter the patient id for which you need to edit the data:')
            print("""1. Patient's ID
2. Patient's Name
3. Date Of Test
4. Result Of RTPCR Test""")
            old=int(input('Enter the number of the data you want to edit:'))
        except:
            x='Enter valid values'
        if (old>5) and (old<1):
            print('Enter valid choice')
            continue
        else:
            modify(pid,old)
            print('The data is modified')
            continue
    elif no==3:
        try:
            pid=input("Enter the patient's id for which you need to delete the data:")
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
        elif num==2:
            pid=input("Enter the patient's id of the data which you need to display:")
            selective(pid)
            continue
    elif no==5:
        print('Thank you for joining in')
        break
    else:
        print('Please enter valid number')
        continue
