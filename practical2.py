#Hemang Vats, XII-A, menu driven program
import os
def add():
    a=open('text.txt','w')
    l=[]
    for x in range (0,4):
        line=input('Enter the line you want to enter:')
        l.append(line+'\n')
    a.writelines(l)
    a.close()
def menu():
    print("""Choose your activity:
1. Replace all the occurrences of the word 'my' by ours
2. count the number of sentences that begin with a'T'""")
def my():
    a=open('text.txt','r')
    temp= open('temp.txt','w')
    m=a.readlines()
    for x in m:
        l=x.split()
        for n in l:
            if n=='my':
                n='ours'+' '
            else:
                n=n+' '
        temp.writelines(l)
    a.close()
    temp.close()
    os.remove(a)
    os.rename(temp,a)
def  count ():
    count=0
    a=open('text.txt','r')
    m=a.readlines()
    for x in m:
        if x[0]=='T':
            count=count+1
        else:
            continue
    a.close()
add()
menu()
choose=int(input('Enter 1 or 2 according to your choice:'))
if choose==1:
    my()
elif choose==2:
    count()
else:
    print('Enter valid choice')
            
    
            
    
