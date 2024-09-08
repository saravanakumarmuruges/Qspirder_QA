st='abc45@90zxyPythON!@#$03'
out=0

for char in st:
    if '0'<=char<='9':
        out+=int(char)
    
print(out)