#1-100的数字 跳过7的倍数和含有7的数
for i in range(1,101):
    if i%7 != 0:
        if '7' not in str(i):
            print(i)