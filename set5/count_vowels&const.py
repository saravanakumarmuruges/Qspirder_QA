st = 'aknkdniou'
vowels = ['a','e','i','o','u']
vow = 0
const = 0
for i in st:
    if i in vowels:
        vow = vow + 1
    else:
        const = const +1

print(f"Count of Vowels : {vow}")
print(f"Count of Const : {const}")