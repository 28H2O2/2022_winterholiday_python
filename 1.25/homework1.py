from functools import reduce

def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    x = 0
    def fn(x, y):
        return x * 10 + y
    for i in range(len(s)):
        if s[i] == '.':
            x = i
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s[:x]))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')