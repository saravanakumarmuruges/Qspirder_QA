io = input("Enter comma separated values to separate +ve and -ve Numbers : ")
li = io.split(',')
neg = [0]*len(li)
pos = [0]*len(li)
pos_index=0
neg_index=0

for i in range(len(li)):
    num = li[i]
    if '1'<=num<='9':
        pos[pos_index] = int(num)
        pos_index +=1
    else:
        neg[neg_index] = int(num)
        neg_index +=1
res_pos = [0]*pos_index
for i in range(pos_index):
    res_pos[i]=pos[i]
    
res_neg = [0]*neg_index
for i in range(neg_index):
    res_neg[i]=neg[i]

print(res_pos)
print(res_neg)