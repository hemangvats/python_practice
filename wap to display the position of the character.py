# Hemang Vats, XI-A, WAP to display the position of the character in a string
str1=input('Enter a string:')
var=input('Enter the character:')
if var in str1:
    f=str1.find(var)
    print('The position of the character is',f+1,'in the string')
else:
    print('The character is not in the string')
   
