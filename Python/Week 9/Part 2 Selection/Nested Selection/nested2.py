

userAge = int(input('Enter age: '))

if userAge > 16 :
    userCode =input('Enter code :')
    if userCode == 'Python':
        print('Access Granted')
    else:
        print('Code is not valid')
else:
    print("Come back when you're over 16")


print('Closing...app')

# exercise
# create a program that ask user 
# for username
# compare the username enered with the hardcoded username value
#if there is a match ask for the password
# if password is a match, print access granted
#if there is no match with username 
#print incorrect username and don't ask further questions
savedUsername = 'admin'
savedPassword = 1234

userName = input('Enter Username : ')

if userName == savedUsername :
    userPassword = int(input('Enter your password: '))
    if userPassword == savedPassword :
        print('Acces Granted')
    else:
        print('Password Incorect')
else:
    print('Username not match')
print('Closing..app')
