st = 'Ananth'
st='MadaM'
rev = ''
for i in range(len(st)-1, -1, -1):
    rev += st[i]

if rev==st:
    print('palindrome')