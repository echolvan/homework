# game_guess21
# author pengtao
'''
- 两个玩家，游戏开始先输入名字
- 用字典保存每个玩家信息：姓名，获胜次数
- 电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21的获胜
- 每轮结束显示玩家信息
- 按q退出游戏
'''
#  输入玩家名字
user01 = input('请输入玩家一姓名')
user02 = input('请输入玩家二姓名')
win1 = 0
win2 = 0

# 进入主程序游戏
i = 'continue'   # 给i赋初值
while i != 'Q' :    
    # pc产生两个随机数与各自玩家输入的数相加
    import random
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    sum1 = int(input(f'{user01}，请输入您猜的数字')) + num1 + num2
    sum2 = int(input(f'{user02}，请输入您猜的数字')) + num1 + num2
    # 判断谁的数与随机数的和相加更靠近21，并输出谁赢此轮游戏
    if abs(sum1-21) == abs(sum2-21) :
            print(f'{user01} and {user02} end in a draw')
    elif abs(sum1-21) < abs(sum2-21) :
        win1 = win1 + 1
        print(f'{user01} win this game!')
    else :
        win2 = win2 + 1
        print(f'{user02} win this game!')
    print(f'{user01} win {win1} times,{user02} win {win2} times')   #输出每轮玩家名字和赢得游戏次数
    #储存每个玩家信息，名字，获胜次数
    inf ={
    'name1' : {user01 : win1},
    'name2' : {user02 : win2},   
    }
    #游戏继续提示
    i = input('是否继续游戏，继续输入（C）退出输入(Q)')
    i = i.upper()
    i = i.strip()
    