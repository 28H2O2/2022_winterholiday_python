class Animal(object):   #编写Animal类
    def run(self):
        print("Animal is running...")

class Dog(Animal):  #Dog类继承Amimal类，没有run方法
    pass

class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')
    pass

class Car(object):  #Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')

class Stone(object):  #Stone类不继承，也没有run方法
    pass

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Car())
# run_twice(Stone())


class plant(object):
    def breath(self):
        print(' it is breathing')
class flower(plant):
    def breath(self):
        print('flower is breathing')
class stone(object):
    pass
p = plant()
f = flower()
p.breath()
f.breath()

def run_twice2(pl):
    pl.breath()
    pl.breath()

run_twice2(flower())