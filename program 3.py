#Hemang Vats,XII-A,to display only 3 lettered words and count them as well
def test():
    f=open('Three.txt','w')
    l=[]
    y='yes'
    while y in ('yes','Yes','y','Y','YES','YeS','YEs','yES','yeS'):
        content=input('Enter the content which you want to wirte in the file:')
        y=input('Do you wish to add more sentences?:')
        l.append(content+' ')
    f.writelines(l)
    f.close()
def test1():
    f=open('Three.txt','r')
    count=0
    l=f.readlines()
    for y in l:
        m=y.split()
        for x in m:
            if len(x)==3:
                count=count+1
            else:
                continue
    print('The number of three lettered words present in the file is',count)
    f.close()
test()
test1()

