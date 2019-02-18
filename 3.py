primr = [] # prime no array

inp_no = 600851475143

# if multple of 2, then add it as multiple
if inp_no % 2 == 0:
    inp_no /= 2
    primr.append(2)

i = 3
while i <= inp_no:
    if inp_no % i == 0:
        inp_no /= i # because prime factors are unique numbers and to reduce computation
        primr.append(i)
        print(primr)
    i+=2 # adding 1 will just bring multiple of 2

print(primr)
