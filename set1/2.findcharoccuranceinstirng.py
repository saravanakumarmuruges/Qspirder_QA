st = input("Enter the string : ")
search_char = input("Enter char to fine in string : ")
count = 0
for i in st:
    if i==search_char:
        count +=1
    
print(f"The given charcter '{search_char}' available {count} time in given string")