from getpass import getpass
password = getpass('password: ')
if password == 'abcd':
    print('welcome strnger!')
else:
    print('wrong password')