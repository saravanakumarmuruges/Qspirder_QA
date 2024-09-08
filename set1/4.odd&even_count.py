''' Programe to find count of Even and Odd numbers in list'''
io = input("Enter comma separated values to find give count of even numbers and odd numbers : ")
li = io.split(',')
odd_count = 0
even_count =0
for i in li:
    if int(i)%2==0:
        even_count +=1
    else:
        odd_count +=1

print(f" Count of ODD Numbers: {odd_count}")
print(f" Count of EVEN Numbers : {even_count}")