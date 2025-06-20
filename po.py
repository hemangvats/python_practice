# Hemang Vats , XI-A, to show what is the character
check='yes'
while check=='yes':
    if check=='yes':
        num= input('Enter a character:')
        if num>='0' and num<='9':
            print('the character is a digit')
        elif num>='a' and num<='z':
            print('the character is an alphabet')
        elif num>='A' and num<='Z':
            print('the character is an alphabet')
        else:
            print('the character is a special character')
        check= input('do you want to continue? yes or no?:')
        continue
    else:
        break
          
