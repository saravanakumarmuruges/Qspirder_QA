# input("Enter comma separated values to count : ")
st = input("Enter string to find product of Numbers in it : ")
out = 1
changed=False
for i in st:
    if '0' <= i <='9':
        out = out * int(i)
        changed = True
    else:
        pass
if changed:
    print(f"Product of numbers in Given string is : {out}")
else:
    print(f"No Number availale in given string : {st}")