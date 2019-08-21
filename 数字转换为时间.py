t=input("请输入一个数字：")

def hours(t):
    while True:
        if t<=0:
            t=int(input("请输入大于0的数字:"))
            continue
        else:
            print("您输入的数字转换结果为{}H{}M".format(int(t/60),t%60))
            break
try:
    hours(int(t))
except:
    print("输入的数字有误！")