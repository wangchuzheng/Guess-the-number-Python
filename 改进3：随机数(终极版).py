import random# 引入模块random（作用：生成随机数）
数 = random.randint(1,10)# 生成一个1-10的随机数，赋值给数变量
print("作者：王楚铮")
次数 = 4
临时 = input("猜猜我想的是哪个数字（1-10）：\n")
guess = int(临时)
while guess != 数 and 次数 != 0:
    临时 = input("猜错啦，请重新输入吧：\n")
    guess = int(临时)
    if guess == 数:
        print("Good\t")
        次数 = 0
    else:
        if guess > 数:
            print("大了大了！")
        else:
            print("小了小了！")
        次数 = 次数 - 1
if guess == 数:
    print("恭喜你，猜对了")
    print("游戏结束！")
else:
    print("游戏结束！")
        
