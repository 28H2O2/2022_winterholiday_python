import pandas as pd
def read():  # 打印
    print(data)
def modify(row1, col1, newvalue):
    data[row1][col1] = newvalue
    read()
def exchange(row1, col1, row2, col2):
    temp = 0
    temp = data.iloc[row1, col1]
    data.iloc[row1, col1] = data.iloc[row2, col2]
    data.iloc[row2, col2] = temp
    read()
def delete(row1, col1):
    data.iloc[row1, col1] = ''
    read()
while True:  # 输入并且若出现错误，提醒重新输入
    file = input('please input your filename:')
    try:
        data = pd.read_excel(file, header=None)
        break
    except FileNotFoundError as e:
        print("please input right filename!", e)

while True:
    func = input('please input your manipulation')
    if func == 'modify' or func == 'exchange' or func == 'delete':
        break
    else:
        print('please input again!')
if func == 'modify':
    a, b, c = map(int, input('输入row1,col1,newValue空格隔开:').split())
    modify(a, b, c)
if func == 'exchange':
    a, b, c, d = map(int, input('输入row1,col1,row2,col2空格隔开:').split())
    exchange(a, b, c, d)
if func == 'delete':
    a, b = map(int, input('输入row1,col1空格隔开:').split())
    delete(a, b)
