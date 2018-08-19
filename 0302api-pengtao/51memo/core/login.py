import pickle
import os
import logging
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import mylog


# logging.disable(logging.CRITICAL)
# 禁止所有日志输出
path = base_path + r'\db'


def register(logger):
    """输入用户名和密码，不存在该用户则注册一个，存在则显示登录成功"""
    log = logger
    name = input('请输入用户名')
    password = input('请输入密码')
    # 生成日志对象
    if 'user.pkl' in os.listdir(path):
        log.debug('文件已存在')
    else:
        filepath = path + r'\user.pkl'
        with open(filepath, 'wb') as f:
            list = {}
            pickle.dump(list, f)

    with open(path + r'\user.pkl', 'rb') as f:
        list = pickle.load(f)
        if name in list.keys():    # 判断是否存在该用户
            if password == list.get(name):    # 验证密码
                print('登录成功')
                log.info(f'{name}登录成功')
                datapath = path + r'\\' + name + '.pkl'
        else:
            list[name] = password
            print('注册成功，欢迎使用51memo')
            log.info('注册成功，欢迎使用51memo')
            with open(path + r'\user.pkl', 'wb') as f:
                pickle.dump(list, f)
            data_name = name + '.pkl'
            datapath = path + r'\\' + data_name
            with open(datapath, 'wb') as f:
                memo_list = []
                pickle.dump(memo_list, f)
            log.debug(f'该{name}用户数据文件已生成')
    return datapath       # 返回数据文件的路径


# def main():
#     """主函数测试该文件"""
#     register()

# if __name__ == '__main__':
#     main()
