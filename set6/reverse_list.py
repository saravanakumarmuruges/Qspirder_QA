li = [1,2,3,4,5,1,3]
start=0
end=len(li)-1

while start<end:
    li[start], li[end] = li[end], li[start]
    start += 1
    end -= 1

print(li)