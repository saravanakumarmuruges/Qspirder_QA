st = 'abc def ghi'
out = ''

for i in st:
    if i == ' ':
        out += '-'
    else:
        out +=i

print(out)