io = input("Enter comma separated values to find give count of even numbers and odd numbers : ")
li = io.split(',')
po_count = 0
neg_count = 0
for i in li:
    if int(i)<0:
        neg_count +=1
    elif int(i) ==0:
        pass
    else:
        po_count +=1

print(f"Positive Number Count : {po_count}")
print(f"Negative number Count : {neg_count}")