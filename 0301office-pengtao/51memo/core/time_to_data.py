import re

class TimeToData:
    def __init__(self, info):
        self.months = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0

    def months_to_data(self, info):
        if re.search('下个月', info):    # TODO为什么十一月十二月用不了
            self.months = 1
        elif re.search('下(.)个月', info):
            word = re.search('下(.)个月', info).group(1)
            self.months = word_to_numb(word)
    
    def days_to_data(self,info):
        days_to_num = {
            '明天':1,
            '后天':2,
            '大后天':3,
        }
        for d in days_to_num:
            if re.search(d, info):
                self.days =  days_to_num[d]
            elif re.search('(.?.?)号', info):
                self.day = word_to_numb(re.search('(.?.?)号', info).group(1))                 
    def weekday_to_data(self, info):
        weeks_to_ = {
            '下周':1,
            '下下周':2,
        }
        weekdays_ = {
            '周一': 'MO',
            '周二': 'THU',
            '周三': 'WED',
            '周四': 'THR',
            '周五': 'FR',
            '周六': 'SAT',
            '周七': 'SUN',
            '周天': 'SUN',
            '周日': 'SUN',
            '礼拜一': 'MO',
            '礼拜二': 'THU',
            '礼拜三': 'WED',
            '礼拜四': 'THR',
            '礼拜五': 'FR',
            '礼拜六': 'SAT',
            '礼拜七': 'SUN',
            '礼拜天': 'SUN',
            '礼拜日': 'SUN',
        }
        for wk in weeks_to_:
            if re.search(wk, info):
                self.weeks =  weeks_to_[wk]
        for wd in weekdays_:        
            if re.search(wd, info):
                self.weekdays = weekdays_[wd]
    
    def hours_to_data(self, info):
        if re.search('下个?钟头', info):
            self.hours = 1

    def minutes_to_data(self):
        pass


def word_to_numb(word):
    """将文字转换为数字，仅支持中文一千以内"""
    if len(word) == 5:
        a, b, c = re.search('(.)百(.)十(.)', word).groups()  # a为百位，b为十位，c为个位
    elif len(word) == 3:
        a = 0
        b, c = re.search('(.)十(.)', word).groups() 
    elif len(word) == 2:
        a =0
        b = '一'
        c = re.search('十(.)', word).group(1)
    elif len(word) == 1:
        a, b = 0, 0
        c = word
    diction = {
        0:0,
        '一':1,
        '二':2,
        '两':2,
        '三':3,
        '四':4,
        '五':5,
        '六':6,
        '七':7,
        '八':8,
        '九':9,
        '十':10
    }
    a = diction[a]
    b = diction[b]
    c = diction[c]
    return a*100 + b*10 + c

print(word_to_numb('五百五十一'))
