st = 'jsbflsj!@#$;,.[]'
out=''
for i in st:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9' or i == ' ':
        pass
    else:
        out +=i
print(out)