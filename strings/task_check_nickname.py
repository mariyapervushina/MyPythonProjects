s = input()
if s[0] == '@':
    if 5 <= len(s) <= 15:
        if s[1:].isalnum() and s[1:] == s[1:].lower():
            print('Correct')
        else:
            print('Incorrect')
    else:
        print('Incorrect')       
else:
    print('Incorrect')


