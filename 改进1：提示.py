临时 = input("猜猜我想的是哪个数字：\n")
guess = int(临时)
if guess == 5:
    print("恭喜你，猜对了！")
else:
    if guess > 5:# 当guess大于5时，执行下面的语句
        print("大了大了！")# 输出"大了大了！"
    else:# 如果不对，执行下面的语句
        print("小了小了！")# 打印"小了小了！"
print("游戏结束！")
    
