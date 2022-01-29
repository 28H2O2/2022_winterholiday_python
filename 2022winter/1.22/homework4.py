digit_list = [1, 324, 41, 324, 423, 1223, 23, 1, 21, ]
max = digit_list[0]
for i in digit_list:
    if max < i:
        max = i
print(max)
