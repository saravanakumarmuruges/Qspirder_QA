li = [1,2,1,2,1,2]
i=0
j=len(li)
while i<len(li):
    for j in range(i):
        if li[i] == li[j]:
            li.pop(i)
            i -=1
            break
    i+=1
print(li)