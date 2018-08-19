# !/usr/bin/env python
# -*- coding=utf-8 -*-

import argparse
import configparser
import os
import logging

import paramiko
from paramiko import SSHException, SSHClient

import config
import control_line
from upload_and_download import upload, download, upload_many
from mylog import log


class AcceptPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


class MySSH:
    def __init__(self, host, password, user):
        self.host = host
        self.password = password
        self.user = user
        try:
            self.client = SSHClient()
            # 我们第一次连接时会去核实host它会去找known_host_key的这个文件，没有按如下处理
            self.client.set_missing_host_key_policy(AcceptPolicy())
            # 我们hostkey不在时的规定:set policy to use when connecting to servers without a known_host_key,然后我们另起炉灶
            self.client.connect(hostname=host, username=user, password=password, timeout=10)
            log.debug(f'{user}成功登录{host}主机')
        except Exception as e:
            print(e)
            log.debug(f'{user}登录{host}主机失败：原因{e}')
            self.client = None

    def send_cmd(self, cmd):
        """发送命令取得返回值"""
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            log.debug(f'{self.user}登录{self.host}执行了{cmd}命令')
            print(stdout, stderr)
            return stdout
        except SSHException as e:
            log.debug(f'{self.user}登录{self.host}执行了{cmd}命令未成功，原因：{e}')
            print(e)

    def close(self):
        """关闭连接"""
        self.client.close()
        log.debug(f'{self.user}登录的{self.host}主机断开连接')


def main():
    cli = control_line.ControlLine()
    cli.run()
    cfg = config.Config()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ssh_login.cfg')

    # 登录服务器
    if cli.args.shell:
        ips = cli.args.filename
        for host_ip in ips:
            if cfg.read_config(config_path, host_ip):
                dic = dict(cfg.read_config(config_path, host_ip))
                user = dic['user']
                password = dic['password']
                host = host_ip
                ssh = MySSH(host=host, password=password, user=user)
                if ssh.client:
                    print('登录成功')
                else:
                    print('登录失败')
            else:
                print(f'配置文件中不含{host_ip}主机')
                log.debug(f'配置文件中不含{host_ip}主机')

    # 上传文件
    elif cli.args.upload:
        if len(cli.args.filename) == 2:
            try:
                local_file = cli.args.filename[0]
                remote_server_file = os.path.join('download/', cli.args.filename[1])
            except Exception as e:
                print(e)
                return None

            ssh = MySSH('192.168.23.129', '2587539619', 'root')
            if ssh.client:
                ret = upload(ssh.client, local_file, remote_server_file)
                print(ret)
        elif len(cli.args.filename) == 0:
            ssh = MySSH('192.168.23.129', '2587539619', 'root')
            if ssh.client:
                upload_many(ssh.client)
        else:
            print('输入参数不合规范')
            print(' 参数一为本地文件，参数二为远程服务器文件')
            log.debug('上传文件时，输入参数不合规范')
    # 下载文件
    elif cli.args.download:
        if len(cli.args.filename) == 2:
            try:
                remote_server_file = cli.args.filename[0]
                local_file = cli.args.filename[1]
            except Exception as e:
                print(e)
                return None
            ssh = MySSH('192.168.23.129', '2587539619', 'root')
            if ssh.client:
                ret = download(ssh.client, remote_server_file, local_file)
                print(ret)
        else:
            log.debug('下载文件时，输入的参数不合规范')
            print('输入参数不合规范')
            print('参数一为远程服务器文件，参数二为本地文件')

    # 控制台交互
    elif cli.args.console:
        ssh = MySSH('192.168.23.129', '2587539619', 'root')
        log.debug('root用户登录192.168.23.129主机操作控制台')
        while True:
            cmd = input('请输入shell命令,[q]-退出')
            if cmd == 'q':
                ssh.close()
                break
            log.debug(f'输入了命令{cmd}')
            stdout = ssh.send_cmd(cmd)
            print(stdout.read().decode())

if __name__ == '__main__':
    main()
