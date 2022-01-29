# import functools


# def log(func):
#     # @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print("hahahaha")


# now()
# print(now.__name__)


import functools 
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        fn(*args, **kw)
        end_time = time.time()
        t = 1000 * (end_time - start_time)
        print('%s executed in %s ms' % (fn.__name__, t))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
