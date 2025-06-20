# Hemang Vats, XI-A, WAP to check whether a string is a palindrome or not
str1=input('Enter a string:')
y=''
str2=str1[::-1]
if (str1==str2):
    print('The word',str1,'is a palindrome')
else:
    print('The word',str1,'is not a palindrome')
