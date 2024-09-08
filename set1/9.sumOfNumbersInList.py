io = input("Enter comma separated values to count : ")
li = io.split(',')
out = 0
for i in li:
    out +=int(i)

print(out)