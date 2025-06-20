#Hemang Vats,XII-A,count number of vowels in the file
def test():
    f=open('Myfile.txt','w')
    l=[]
    y='Yes'
    while y in('yes','Yes','y','Y','YES','YeS','YEs','yES','yeS'):
        content=input('Enter your content which you want to enter in the file:')
        y=input('Do you wish to add more statements?:')
        l.append(content)
    f.writelines(l)
    f.close()
def test1():
    f=open('Myfile.txt','r')
    count=0
    l=f.read()
    for x in l:
        if x in'aeiouAEIOU':
            count=count+1
        else:
            continue
    print('The number of vowels present in the file is',count)
    f.close()
test()
test1()
