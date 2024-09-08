'''
WAP TO PRINT VOWEL CHARACTERS FROM THE STRING IF LENGTH OF THE STRING IS EVEN. 
ELSE PRINT CONSONENT CHARACTERS FROM THE STRING.
'''
st = 'santhoshi'
vow = ['a','e','i','o','u'] 
i=0


if len(st) %2 ==0:
    while i<len(st):
        if st[i] in vow:
            print(st[i])
        i=i+1
else:
    while i<len(st):
        if st[i] not in vow:
            print(st[i])
        i=i+1