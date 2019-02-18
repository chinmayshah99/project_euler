sum1 = 2
t1 = 1
t2 = 2
while t2 < 4000000:
    t1, t2  = t2, t1 + t2
    if t2 % 2 == 0:
        sum1 += t2
        print(str(t2) + " ,", end = '')

print('')    
print(sum1)