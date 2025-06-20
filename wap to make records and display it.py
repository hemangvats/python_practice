# Hemang Vats, XI-A, WAP to accept roll no,marks,names and make a record
record=[]
l=[]
for x in range(1,6):
    rollno=int(input('Enter Roll no:'))
    l.append(rollno)
    name=input('Enter Name:')
    l.append(name)
    marks=int(input('Enter Marks:'))
    l.append(marks)
    record.append(l)
    l=[]
for y in record:
        display=y
        print('roll no.:',display[0],sep='')
        print('Name:',display[1],sep='')
        print('marks:',display[2],sep='')
        print()
        
    
    
