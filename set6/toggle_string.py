st = 'AbCdeFGh'
out = ''

for i in st:
    if 'a'<=i<='z':
        out +=chr(ord(i)-32)
    elif 'A'<=i<='Z':
        out +=chr(ord(i)+32)
    else:
        out +=i

print(out)