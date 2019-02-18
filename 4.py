highest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        new_str = str(i * j)
        if (new_str)[: : -1] == (new_str):
            temp = int(new_str)
            if temp > highest:
                highest = temp

print(highest)