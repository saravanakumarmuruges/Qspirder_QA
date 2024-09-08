st = 'aaaBBBBbCCCCddDDDeeeeeeeFFFF'
out = ''
for char in st:
    if 'a'<=char<='z':
        out += chr(ord(char)-32)
    else:
        out +=char
    
print(out)