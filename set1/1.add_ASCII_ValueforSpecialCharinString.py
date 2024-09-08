st = input("Enter string to get ASCII for special charcters : ")
out = ''
for char in st:
    if 'a' <= char <= 'z' or 'A' <=char <= 'Z' or '0' <=char <= '9' or char == ' ':
        out +=char
    else:
        out += str(ord(char))

print(out)