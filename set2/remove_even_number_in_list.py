li = [1,2,3,4,5]


for i in range(len(li) - 1, -1, -1):
    if li[i] %2 ==0:
        li.pop(i)

print(li)