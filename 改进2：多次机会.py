print("作者：王楚铮")
次数 = 3
临时 = input("猜猜我想的是哪个数字（1-10）：\n")
guess = int(临时)
while guess != 5:
    临时 = input("猜错啦，请重新输入吧：\n")
    guess = int(临时)
    if guess == 5:
        print("Good\t")
    else:
        if guess > 5:
            print("大了大了！")
        else:
            print("小了小了！")
        if 次数 != 0:# 如果次数不等于0，执行下面的语句
            次数 = 次数 - 1# 将变量次数的值减1
        else:# 如不是，执行下边的代码
            break# 跳出循环体
if guess == 5:
    print("恭喜你，猜对了")
    print("游戏结束！")
else:
    print("游戏结束！")
        
