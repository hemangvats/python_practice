def test(num1,num2,num3=5):
    if num1>num2 and num1>num3:
        return('num1 is the largest number',num1)
    elif num2>num1 and num2>num3:
        return('num2 is the largest number',num2)
    elif num3>num1 and num3>num2:
        return ('num3 is the largest number',num3)
    else:
        return ('all the numbers are equal')
var1=int(input('Enter a number:'))
var2=int(input('Enter a number:'))
var3=int(input('Enter a number:'))
x=test(var1,var2,var3)
print(x)

