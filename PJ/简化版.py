import itertools

a, b, c, d, e, f, g, h, i, j = range(10)
Graph = [{1, 7, 8, 3}, {3, 9, 0, 5}, {5, 6, 7, 2},
         {2, 8, 9, 4}, {4, 0, 6, 1}]
x1, x2 = map(int, input("请输入0-24中的两个数字，中间用空格隔开:").split())
star_pos = [x1, x2]

list1 = set([z for z in range(10)])
list1.remove(x1)
list1.remove(x2)
result = itertools.combinations(list1, 3)  # 直接取组合
all = list(result)


def check(cc):     # 检验每个集合是否符合条件
    flag = True
    for j in range(5):     # 遍历集合里的元素
        flag1 = 0
        for i in range(3):       # 遍历Graph
            if cc[i] in Graph[j]:
                flag1 += 1
        if x1 in Graph[j]:            # 循环结束之后判断s,h
            flag1 += 1
        if x2 in Graph[j]:
            flag1 += 1
        if flag1 == 2:      # 若恰有两个则成立
            flag = True
        else:
            flag = False
            break          # 有任何一组不满足则直接退出
    return flag


if check((3, 4, 5)):
    print(111)

if __name__ == '__main__':     # 主程序
    for z in all:
        if check(z):
            z1 = list(z)       # 变成list之后插入原有元素，输出
            z1.append(x1)
            z1.append(x2)
            z1.sort()
            print(z1)
