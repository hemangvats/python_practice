# Hemang Vats, XI-A, WAP to display characters which are common in two strings
str1=input('Enter a string:')
str2=input('Enter another string:')
list1=list(str1)
list2=list(str2)
for x in list1:
    for y in list2:
        if x==y:
            print(x,'is present in both the strings')
        else:
            continue
if x!=y:
    print('No alphabet is common in both the strings')
    
