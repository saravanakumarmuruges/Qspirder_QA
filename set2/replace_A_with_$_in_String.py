st = 'AbcaedfeessA'
out = ''
for char in st:
    if char == 'A':
        out += '$'
    else:
        out +=char 
        
print(out)