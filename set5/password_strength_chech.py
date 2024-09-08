passwd = 'Saravanan@3'
upper_flag = False
lower_flag = False
schar_flag = False
num_flag = False
for i in passwd:
    if 'a'<=i<='z':
        lower_flag=True
    elif 'A'<=i<='Z':
        upper_flag=True
    elif '0'<=i<='9':
        num_flag=True
    elif i ==' ':
        pass
    else:
        schar_flag=True

if upper_flag and lower_flag and schar_flag and num_flag:
    print('Password is strong')
else:
    print('Week Password')