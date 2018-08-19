
class Temperature:
    "华氏温度和摄氏温度的互换"
    def C_to_F(self,celsius):
        "摄氏度转华氏度"
        fahrenheit = 32 +(9/5)* celsius
        fahrenheit = format(fahrenheit, '.2f')
        print(f'{celsius}摄氏度等于{fahrenheit}华氏度')
    

    def F_to_C(self,fahrenheit):
        "华氏度转摄氏度"
        celsius = (fahrenheit - 32)*(5/9)
        celsius = format(celsius, '.2f')
        print(f'{fahrenheit}华氏度等于{celsius}摄氏度')


class Currency:
    "美元转换人民币，人民币转换美元"
    def usd_to_rmb(self, usd):
        "美元转人民币"
        rmb = 0
        rmb = usd*6.33
        print(f'{usd}美元可兑换{rmb}人民币')


    def rmb_to_usd(self, rmb):
        "人民币转美元"
        usd = 0 
        usd = rmb/6.33
        print(f'{rmb}人民币可兑换{usd}美元')


class Length:
    "英尺和米制的互换"
    def m_to_inch(self,meter):
        '米换为英尺'
        inch = 0
        inch = meter*3.28
        print(f'{meter}米等于{inch}英尺')

    def inch_to_m(self,inch):
        '英尺换为米'
        meter = 0
        meter =inch/3.28
        print(f'{inch}英尺等于{meter}米')


class Transfer:
    def choose_to_print(self,a_string):
        '''根据不同的输入内容，自动选择相应功能类去处理逻辑，并输出 温度：从结尾的c或f，或摄氏度和华氏温度'''
        import re
        temp = sum([int(x) for x in re.findall(r'\d+',a_string)])
        # 将转换量的大小提取出来，并转为整型的数据保存
        if re.match(r'(\d+)c|(\d+)f',a_string):
            if re.match(r'(\d+)c|(\d+)f',a_string):
                if re.match(r'(\d+)c',a_string):
                    t = Temperature()
                    t.C_to_F(temp)
                else:
                    t = Temperature()
                    t.F_to_C(temp)
        elif  re.match(r'(\d+)m|(\d+)in',a_string): 
            if re.match(r'(\d+)m',a_string):
                l = Length()
                l.m_to_inch(temp)
            else:
                l = Length()
                l.inch_to_m(temp)
        else:
            if re.match(r'(\d+)usd',a_string):
                c = Currency()
                c.usd_to_rmb(temp)
            else:
                c =Currency()
                c.rmb_to_usd(temp)


def welcome():
    '欢迎界面'
    print('欢迎使用echolvan的translator'.center(30,"*"))


def main():
    '主函数调用其他函数完成转换功能'
    y = 1
    while y:
        welcome()
        a_string = input('请输入转换量')
        trans = Transfer()
        trans.choose_to_print(a_string.lower())
        y = input('继续请按1，退出请按0')

if __name__ == '__main__':
    main()



