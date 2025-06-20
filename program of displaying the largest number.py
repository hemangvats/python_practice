#Hemang Vats
# Accepting 3 numbers and displaying largest number
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
if(num1>num2 and num1>num3):
    print(num1,"is the largest number")
elif(num2>num1 and num2>num3):
    print(num2,"is the largest number")
elif(num3>num1 and num3>num2):
    print(num3,"is the largest number")
else:
    print("All the numbers are equal")
