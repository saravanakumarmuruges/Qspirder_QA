io = input("Enter comma separated values to find give sum of Even Numbers and product of ODD Numbers :\n")
li = io.split(',')
even_sum = 0
odd_product = 1
for i in li:
    if int(i)%2==0:
        print(i)
        even_sum = even_sum + int(i)
    else:
        odd_product = odd_product * int(i)


print(f"Sum of Even Numbers: {even_sum}")
print(f"Product of Odd Numbers : {odd_product}")