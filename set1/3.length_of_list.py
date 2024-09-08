''' Code to find length of list without using inbuilt functions'''
io = input("Enter comma separated values to count : ")
li = io.split(',')
count=0
for i in li:
    count +=1

print(f"Total number of items provided is : {count}")