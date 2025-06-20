# Hemang Vats,XII-A,to display the sentences which starts with the
def test():
    f=open('hello.txt','w')
    l=[]
    x='y'
    while x in('yes','Yes','y','Y','YES','YeS','YEs','yES','yeS'):
        content=input('Enter the content which you want to wirte in the file:')
        l.append(content+'\n')
        x=input('do you wish to add more lines?:')
    f.writelines(l)
    f.close()
def test1():
    f=open('hello.txt','r')
    l=f.readlines()
    for x in l:
        m=x.split()
        if m[0]=='The':
            print()
            print(x)
        else:
            continue
    f.close()
test()
test1()
