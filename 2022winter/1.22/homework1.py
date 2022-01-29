
ans = 99
gue = 0
count = 0
while count < 3:
    gue = input("please enter your guess\n")
    if gue.isdigit():
        gue = int(gue)
    else:
        print("The input is wrong !")
        exit()
    if(gue > ans):
        print("it is higher than ans")
    elif(gue < ans):
        print("it is lower than ans")
    else:
        print("you are right!!!!")
        break
    count = count + 1
    if(count == 3):
        flag = input("do you want try again y/n")
        if flag in ["y", "Y", "YES", "yes"]:
            count = 0
        else:
            break
