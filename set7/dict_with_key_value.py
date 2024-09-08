'''CREATE DICTIONARY OF KEYS FROM 1 TO N AND VALUES ARE SQUARE OF KEYS'''

n=5
i=1
out = {}
# method 1
while i<=n:
    out[i]=i**2
    i=i+1

print(out)

#method 2
del out
out={}
for i in range(n,0,-1):
    out[i]=i**2

print(out)