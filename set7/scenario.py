'''PRINT THE NUMBER FROM 1 TO 100 
IF THE NUMBER DIVISIBLE BY 3 PRINT 'FIZZ' OR 
IF THE NUMBER IS DIVISIBLE BY 5 PRINT 'BUZZ' OR 
IF THE NUMBER IS DIVISIBLE BY 3 AND 5 'FIZZ BUZZ' 
ELSE  PRINT THE NUMBER AS IT IS.'''

n=100

for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print('FIZZ BUZZ')
    elif i%3 == 0:
        print('FIZZ')
    elif i%5 == 0:
        print('BUZZ')
    else:
        print(i)