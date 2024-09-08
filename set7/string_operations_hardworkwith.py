st = "Hardwork with knowledge and being honest never fails"

# Getting in list
out1 = st.split(' ')
print(out1)

# Getting in dict with length
out2 = {}
for wd in out1:
    out2[wd]=len(wd)
print(out2)


# Getting getting reversed words.
out3=[''] * len(out1)
for i in range(len(out1)):
    out3[i] = out1[i][::-1]
print(out3)

# Getting word count and Alphabet char count:
word_count=0
alpha_count = 0
for i in range(len(st)):
    if st[i] == ' ' and st[i-1] != ' ':
        word_count += 1
    if 'a' <= st[i] <= 'z' or 'A' <= st[i] <= 'Z':
        alpha_count += 1
    if i == len(st)-1 and st[i] != ' ':
        word_count+=1
    
print(word_count)
print(alpha_count)