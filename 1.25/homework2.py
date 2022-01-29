from functools import reduce
def is_palindrome(n):
    # def iter():
    #     n = 1
    #     while True:
    #         yield n
    #         n += 1
    def fn(x, y):
        return x * 10 + y
    x = n
    L = []
    while n > 0:
        L = L + [n % 10]
        n = n // 10
    return reduce(fn, L) == x
    # it = iter()
    # y = 1
    # while True:
    #     filter(huiwen(y), it)
    #     y += 1
# 测试:
output = filter(is_palindrome, range(100, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')