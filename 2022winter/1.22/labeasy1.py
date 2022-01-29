from email.utils import localtime
import time

# print ("time.time(): %f " %  time.time())
# print (time.localtime( time.time() ))
# print (time.asctime( time.localtime(time.time()) ))

localtime = time.localtime( time.time() )
def timeTest():
    i = 1
    flag = 1 
    while(flag < 9 and localtime.tm_sec != 0):
        print(i)
        i *= 2
        flag += 1
        time.sleep(5)
timeTest()
