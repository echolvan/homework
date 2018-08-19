import pickle
import re


class MemoAdmin:
    """添加MemoAdmin类，作为主体程序，管理Memo类构成的列表，进行Memo的增删改查，处理输入输出"""
    def __init__(self, memo_list):
        self.memo_list = memo_list

    def add(self):
        "实例化Memo，添加到实例化MemoAdmin的对象里"
        info = input('请输入id，name，thing，date！之间用逗号隔开')
        my_memo = Memo.new_memo(info)
        self.memo_list.append(my_memo)
        print('已经成功添加')

    def delete(self):
        "删除要选择的memo"
        num = 0
        for x in self.memo_list:
            print(num, x.thing, x._date)
            num += 1
        i = input('请选择你要删除的memo')
        i = int(i)
        del self.memo_list[i]
        print('已经删除')

    def modify(self):
        "修改memo_list中memo"
        num = 0
        for x in self.memo_list:
            print(num, x.thing, x._date)
            num += 1
        index = input('请选择你要修改的memo')
        index = int(index)
        while True:
            i = input('请选择修改的内容,name(1),thing(2),date(3)')
            if re.match(r'[1-3]', i):
                break
            else:
                print('请重新输入')
            i = int(i)
        if i == 3:
            self.memo_list[index]._date = input('请输入date')
        elif i == 2:
            self.memo_list[index].thing = input('请输入thing')
        else:
            self.memo_list[index].name = input('请输入name')

    def query(self):
        "查询memo_list里的memo"
        num = 0
        for x in self.memo_list:
            print(num, x.thing, x._date)
            num += 1
        y = 1
        while y:
            try:
                i = input('请选择你要查询的memo')
                i = int(i)
                while True:
                    num = input('请选择查询的内容,name(1),thing(2),date(3)')
                    if re.match(r'[1-3]', num):
                        num = int(num)
                        break
                    else:
                        print('请重新输入')
                    num = int(num)
                if num == 3:
                    print(f'{self.memo_list[i]._date}')
                elif num == 2:
                    print(f'{self.memo_list[i].thing}')
                else:
                    print(f'{self.memo_list[i].name}')
            except Exception:
                print('输入超出memo范围')
            y = int(input('继续查询按1，退出按0'))


class Memo:
    "memo的内容"
    def __init__(self, id, name, thing, date):
        "给memo初始化"
        self.___id = id
        self.name = name
        self.thing = thing
        self._date = date

    @classmethod
    def new_memo(cls, info):
        "利用输入的info给类实例化"
        __id, name, thing, _date = info.split(',')
        return cls(__id, name, thing, _date)

    @property
    def id(self):
        "把ID设置为只读"
        return self.___id


def main(user_data):
    "主函数调用方法实现memo_list的增删改查"
    try:
        with open(user_data, 'rb') as f:
            memo_list = pickle.load(f)
    except Exception:
        with open(user_data, 'wb') as f:
            my_memo = []
            pickle.dump(my_memo, f)
    admin = MemoAdmin(memo_list)
    y = 1
    while y:
        choice = input('请选择操作：add（1），del（2），modify（3），query（4）')
        while 1:
            "保证选择在1-4中"
            if re.match(r'[1-4]', choice):    # 在while循环里判断输入是否超出操作范围，提高容错率
                choice = int(choice)
                break
            else:
                print('请重新输入')
                choice = int(choice)
# 每个数字对应不同的增删改查的操作
        if choice == 1:
            admin.add()
        elif choice == 2:
            admin.delete()
        elif choice == 3:
            admin.modify()
        else:
            admin.query()

        y = int(input('继续（1）退出(0)'))
        if y == 0:
            print(admin.memo_list)
        with open(user_data, 'wb') as f:
            f.write(pickle.dumps(admin.memo_list))
if __name__ == '__main__':
    main()
