io = input("Enter comma separated values to get product of it : ")
li = io.split(',')
out=1

for i in li:
    out = out*int(i)
    
print(f" PRODUCT of numbers in Given list : {out}")