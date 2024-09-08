li = [1,2,3,4,5]
out=[0] * len(li)
j=0
for i in range(len(li)-1, -1,-1):
    out[j]=li[i]
    j+=1

print(out)