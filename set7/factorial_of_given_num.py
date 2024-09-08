
num = 5
out = 1
# Method1
for i in range(num, 0, -1):
    out *=i
    
print(f"factorials of give number : {out}")

# Method 2
out=1
i=1
while i<=num:
    out*=i
    i+=1
    
print(f"factorials of give number : {out}")