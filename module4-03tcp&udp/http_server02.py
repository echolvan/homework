#!/usr/bin/env Python
# -*- coding:utf-8 -*-


import socket
import re
import os
import json


EXC_PATH = os.path.dirname(os.path.abspath(__file__))
HOST = ''  # localhost:本机，ip值 ， 空：任意主机都可访问，
# 我这里是用本机作为服务器，让虚拟机进行访问，设置ip值就那个ip的客户端就能访问
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # udp相关参数
# AF_INET表示使用ipv4，由于tcp协议使用的是流传输，所以sock_stream
# 服务器绑定地址
sock.bind(ADDR)

# 监听连接个数
sock.listen(1)
print('tcp服务启动')


def read_html():
    """读取html作为response body"""
    with open(f'{EXC_PATH}/html/homepage.html', 'r') as f:
        html = f.read()
    return html


def read_json():
    """读取json并转为str形式作为resonse body"""
    with open(f'{EXC_PATH}/json/test.json', 'r') as f:
        json_content = str(json.load(f))
    return json_content


def path_to_file(path):
    """根据path来选择返回内容"""
    dic = {
        '/': read_html(),
        '/json': read_json()
    }
    if path in dic.keys():
        # 如果符合'/'和'/json'就返回相应内容
        return dic[path]
    elif re.match(r'/pic/(.*?.jpg)', path).group(1) in os.listdir(f'{EXC_PATH}/pic/'):
        # 否则匹配路径
        pic_path = re.match(r'/pic/(.*?.jpg)', path).group(0)
        with open(f'{EXC_PATH}{pic_path}', 'rb') as f:
            f_data = f.read()
        return f_data
    else:
        return f'没有该{path}资源'

# 等待连接
while True:
    print('等待连接')
    connection, addr = sock.accept()   # connection也是一个socket
    print('成功连接: ', addr)
    # 等待接收
    data = connection.recv(BUFSIZE)   # recv()是用于tcp， recvfrom用于udp
    # 请求数据为空，结束本次连接
    if not data:
        connection.close()
        continue
    while data:
        try:
            # 解析请求头，获得请求路径path
            request_header = data.decode()
            first_info = request_header.splitlines()[0]
            method, path, protocol = first_info.split(' ')
            print('收到数据: ', data.decode())
            print(f'转跳到{path}')

            response_body = path_to_file(path)   # 根据path选择回复内容
            response_first_line = 'HTTP/1.1 200 OK\r\n'
            response_headers = 'Server:My server\r\n'
            # 当回复内容为图片时，另外定制相应头
            if re.match(r'/pic/.*?.jpg', path) and re.match(r'/pic/(.*?.jpg)', path).group(1) in os.listdir(f'{EXC_PATH}/pic/'):
                response_first_line = f"""HTTP/1.1 200 OK
Connection: Keep-Alive
Accept-Ranges: bytes
content-type: image/jpeg

"""
                response = response_first_line + response_body
                connection.sendall(response.encode('gbk'))
                # connection.sendall(response_body)
            else:
                response_headers = 'Server:My server\r\n'
                response = response_first_line + response_headers + '\r\n' + response_body
                connection.sendall(response.encode('gbk'))  # 在这里处理数据,然后发给客户端
            print('成功发送给客户端')
            connection.close()
            break
        except Exception as e:
            print(e)
            connection.close()
            break

# 关闭socket
sock.close()