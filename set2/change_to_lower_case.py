st = 'ABccDDEEff'
out=''
for char in st:
    if 'A'<=char<='Z':
        out+=chr(ord(char)+32)
    else:
        out+=char
print(out)