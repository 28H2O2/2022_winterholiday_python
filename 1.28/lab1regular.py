import re


def testMai(telephone, mail):
    flag1 = False
    flag2 = False
    if re.match(r'^\d{11}$', telephone, flags=0):
        flag1 = True
    if re.match(r'^\w+@\w+.[a-zA-Z0-9._]+$', mail, flags=0):
        flag2 = True
    if flag1:
        if flag2:
            print("The telephone is right and the mail is right!")
        else:
            print("The telephone is right and the mail is wrong!")
    else:
        if flag2:
            print("The telephone is wrong and the mail is right!")
        else:
            print("The telephone is wrong and the mail is wrong!")


testMai('18458837490', 'cyhong@m.fudan.edu.cn')
