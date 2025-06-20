# Hemang Vats, XI-A, WAP to display the percentage as well as grade
def calc(marks):
    percentage=(marks/50)*100
    if percentage>=80:
        return('You have obtained',percentage,'%','You have obtained grade A')
    elif percentage>=60 and percentage<80:
        return('You have obtained',percentage,'%','You have obtained grade B')
    else:
        return('You have obtained',percentage,'%','You have obtained grade C')
marks=int(input('Enter marks:'))
z=calc(marks)
count=0
for x in z:
    count+=1
    if count<len(z):
        print(x,end=' ')
    else:
        print()
        print(x)
