# This program prints 1-10 but skips 8

i = 0 # Counter

while i <= 9:
    i = i + 1
    if i == 8:
        continue
    print(i)
else:
    print('\nThe program has ended')



# This program is meant to print 1-10 and skip 8.
# It runs indefinitely until a break.

i = 1 # loop variables

j = 1

while i <= 10:
    print('Iteration ', j)
    if j >= 15:
        break # loop escape sequence
    j = j + 1
    
    if i == 8:
        continue # indefinite loop
    print('\tvalue =',i)
    i = i + 1
else:
    print('\nThe program has ended')
