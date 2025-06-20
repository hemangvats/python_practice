# Hemang Vats , XII-A, WAP to Count the number of times a string occurs in the file
def test():
    f=open('A.txt','w')
    l=[]
    x='y'
    while x in('yes','Yes','y','Y','YES','YeS','YEs','yES','yeS'):
        content=input('Enter the content which you want to wirte in the file:')
        l.append(content+'\n')
        x=input('do you wish to add more lines?:')
    f.writelines(l)
    f.close()
def test1(str1):
    f=open('A.txt','r')
    l=f.readlines()
    count=0
    for x in l:
        y=x.split()
        for z in y:
            if z==str1:
                count=count+1
            else:
                continue
    print(count)
    f.close()
test()
str1=input('Enter the substring which you want to check in the file:')
test1(str1)
