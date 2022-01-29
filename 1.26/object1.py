class Person(object):
# 这里就是初始化你将要创建的实例的属性
    def __init__(self,hight,weight,age):
        self.hight = hight
        self.weight = weight
        self.age = age

# 定义你将要创建的实例所有用的技能
    def paoniu(self):
        print('你拥有HCY的技能')

    def eat(self):
        print('you can eat')

# 开始创建实例
zhangsan=Person(170,50,29)
lisi = Person(175,100,30)

# 你的实例开始使用它的技能
zhangsan.paoniu()
lisi.eat()


class stu(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def print(self):
        print('%s'%(self.name))
aaa = stu('ax', 111)
aaa.print()
