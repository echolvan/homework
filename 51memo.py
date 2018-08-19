
# coding: utf-8


print('欢迎使用51备忘录'.center(30,'*'))   #欢迎界面


date=[]
things=[]
memo ={'时间': date,
        '事件': things
        }
# 输入备忘事件
a_str = input('请输入你的备忘事件')
a_str.find('今')
a_str_index =a_str.find('今')
print(a_str_index)
# 判断日子
if a_str.find('今') == -1 :
    
    if a_str.find('明') == -1:
        date.append(a_str[a_str.find('后天'):a_str.find('后天')+2])
        print(date)
    else :
        date.append(a_str[a_str.find('明'):a_str.find('明')+2])
else :
    date.append(a_str[a_str.find('今'):a_str.find('今')+2])
exactly_time =['上午','下午','晚上','早上','早晨']
# 利用循环查找具体时间
for i in exactly_time :
    if a_str.find(i) != -1 :
        date.append(a_str[a_str.find(i):a_str.find(i)+2])
        print(date) 
        thing_index = a_str.find(i) + 2
        break
# 判断时刻
if a_str.find('点') != -1 :
    date.append(a_str[a_str.find('点') - 1:a_str.find('点') + 1])
    thing_index = a_str.find('点') + 1       
if a_str.find('分') != -1 :
    date.append(a_str[a_str.find('分') - 1:a_str.find('分') + 1])
    thing_index = a_str.find('分') + 1
    print(date)
things.append(a_str[thing_index:])
print(things)
#彩色输出时间和事件
from color_me import Colorme
print(Colorme(f'事件{things}').blue())
print(Colorme(f'时间{time}').red())
