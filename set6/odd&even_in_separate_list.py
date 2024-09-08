li = [1,2,3,4,5,6,7,8]
odd = [0]*len(li)
even = [0]*len(li)
even_index=0
odd_index=0
for i in range(len(li)):
    if li[i] %2 ==0:
        even[even_index] = li[i]
        even_index +=1
    else:
        odd[odd_index] = li[i]
        odd_index +=1

final_even = [0] * even_index
for i in range(even_index):
    final_even[i] = even[i]

final_odd = [0] * odd_index
for i in range(odd_index):
    final_odd[i] = odd[i]

print(final_even)
print(final_odd)