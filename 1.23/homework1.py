def trim(s):
    while True:
        if s == '':
            break
        if s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-2]
        else:
            break
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!')