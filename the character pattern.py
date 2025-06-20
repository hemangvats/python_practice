def test(character,number):
    x=number
    while x>0:
        y=x
        while y>0:
            print(character,end=' ')
            y=y-1
        x=x-1
        print()
    x=2
    while x<=number:
        y=1
        while y<=x:
            print(character,end=' ')
            y=y+1
        x=x+1
        print()
ch=input('Enter the character:')
num=int(input('Enter a number:'))
test(ch,num)
