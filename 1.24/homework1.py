def findMinAndMax(L):
    # if len(L) == 0:
    if L == []:
        return (None, None)
    max1 = min1 = L[0]
    for i in L:
        if max1 < i:
            max1 = i
        if min1 > i:
            min1 = i
    # max1 = max(L)
    # min1 = min(L)
    return (min1, max1)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')