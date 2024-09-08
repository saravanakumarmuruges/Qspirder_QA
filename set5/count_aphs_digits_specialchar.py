st = 'asafsd123q2@#$ addss!9'
char = 0
num = 0
schar = 0
for i in st:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        char +=1
    elif '0'<=i<='9':
        num +=1
    elif i == ' ':
        pass
    else:
        schar +=1

print(f'Aplhabets in given String : {char}')
print(f'Numbers in given String : {num}')
print(f'SpecialCharcter in given String : {schar}')