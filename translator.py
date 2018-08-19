
# coding: utf-8

# In[1]:

print('欢迎使用单位转换器'.center(30,'-'))  #欢迎界面


# In[8]:

menu = {
    't' : '温度转换',
    'c' : '货币转换',
    'l' : '长度转换',
}
#可选择的转换量菜单



for k,v in menu.items() :   #打印显示可选择的转换量菜单
    print(k,v)


choose = input('请输入转换量，比如：t(温度)')   #输入转换量类型



choose = choose.strip()     #去除输入量前后空格，增加辨识度
choose = choose.lower()     #将输入量类型小写，增加辨识度


if choose == 't' :     #判断输入转换量是否为温度量
    temp = input('请输入温度，比如1C（1摄氏度）  ')     #输入温度
    temp = temp.upper()         #将输入量类型大写，增加辨识度
    if temp.endswith('C') :     #判断是否从摄氏度转为华氏温度
        Tf = (9/5) * float(temp.strip('C')) + 32    #华氏温度转换式
        print(f'{temp}等于{Tf}F')     #输出华氏温度
    else :   #否则输出摄氏度
        Tc = (float(temp.strip('F')) - 32) * (5/9)
        print(f'{temp}等于{Tc}C')
elif choose =='c' :   #判断是否为货币转换
    temp = input('请输入货币类型，比如1RMB(1人民币)')    #输入货币金额
    temp = temp.upper()    #将输入量类型大写，增加辨识度
    if temp.endswith('RMB'):     #判断是否为人民币
        Cusd = 0.1589 * float(temp.strip('RMB'))   #人民币兑换美元
        print(f'{temp}可兑换{Cusd}USD')     #输出美元额
    else :    #否则输出人民币额
        Crmb = 6.2945 * float(temp.strip('USD'))     
        print(f'{temp}可兑换{Crmb}RMB')
else :     #输入量为长度
    temp = input('请输入长度，比如1M(1米)')    #输入长度
    temp = temp.upper()    #将输入量类型大写，增加辨识度                
    if temp.endswith('M') :    #判断长度是否是以米输入
        Lft = float(temp.strip('M')) * 3.28    #将米转换为英尺
        print(f'{temp}等于{Lft}FT')       #输出英尺
    else :     #否则将英尺转换为米，输出米
        Lm = float(temp.strip('FT')) / 3.28
        print(f'{temp}等于{Lm}M')
        
        
     






