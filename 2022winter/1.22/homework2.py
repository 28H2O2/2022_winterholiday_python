rate = 1.01
sum = 10000.0
i = 0
while sum < 20000:
    sum = sum*rate
    i += 1
    print(i, sum)
else:
    print(i)
    print(sum)
