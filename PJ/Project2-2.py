import time

# 初始化
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y = range(25)
Graph = [{a, c, e, f, g}, {a, b, x, m, l}, {a, v, w, t, r}, {d, c, b, v, u},
         {d, e, x, p, o}, {d, f, h, i, j}, {g, h, x, s, r}, {g, i, k, y, l},
         {j, k, x, w, u}, {j, y, m, n, o}, {l, n, p, q, r}, {o, q, s, t, u}]
x1, x2 = map(int, input("请输入0-24中的两个数字，中间用空格隔开:").split())
star_pos = [x1, x2]
list1 = set([z for z in range(25)])
list1.remove(x1)
list1.remove(x2)


def check(cc):     # 检验每个集合是否符合条件(是否恰好每个集合中有两个元素)
    flag = True
    for j in range(12):     # 遍历集合里的元素
        flag1 = 0
        for i in range(len(cc)):       # 遍历Graph
            if cc[i] in Graph[j]:
                flag1 += 1
        if x1 in Graph[j]:            # 循环结束之后判断x1,x2
            flag1 += 1
        if x2 in Graph[j]:
            flag1 += 1
        if flag1 <= 2:      # 若小于两个则成立
            flag = True
        else:
            flag = False
            break          # 有任何一组不满足则直接退出
    return flag


def check2(cc):     # 检验第一次筛选出的集合是否符合条件
    flag = True
    for j in range(12):     # 遍历集合里的元素
        flag1 = 0
        for i in range(8):       # 遍历Graph
            if cc[i] in Graph[j]:
                flag1 += 1
        if x1 in Graph[j]:            # 循环结束之后判断x1,x2
            flag1 += 1
        if x2 in Graph[j]:
            flag1 += 1
        if flag1 == 2:      # 若恰有两个则成立
            flag = True
        else:
            flag = False
            break          # 有任何一组不满足则直接退出
    return flag


def arrange(tup=list()):    # 类似于八皇后的生成方法(generator)
    for new in list1:          # 添加新的元素
        if new in tup:          # 若新元素已经存在则break
            break
        tup1 = tup + [new]
        if check(tup1):
            if len(tup) == 7:     # 判断是否到达最后一个
                yield [new]
            else:
                for result in arrange(tup + [new]):     # 如果不是最后一个则进入递归
                    yield [new] + result


start = time.time()    # 检查程序运行时间

if __name__ == '__main__':     # 主程序
    for z in arrange():     # 通过第一个检查
        if check2(z):       # 第二次检查
            z1 = z + [x1, x2]
            z1.sort()
            print(z1)


end = time.time()
print('Running time: %s Seconds' % (end-start))
