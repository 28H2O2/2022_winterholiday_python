# 测试数据
# want1 = '7_This_is_a_test'
# actual1 = '_hs_s_a_es'  
want = input()
actual = input()
def testKeyBoard(wantInput, actualInput):
    s = set()
    for i in wantInput:
        if i not in actualInput:     # 检验i是否在aactualInput中
            if i >= 'a' and i <= 'z':
                i = chr(ord(i)-32)  # 排除小写字母（将小写变成大写）
            s.add(i)
    return(s)
print(testKeyBoard(want, actual))
