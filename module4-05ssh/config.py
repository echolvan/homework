# !/usr/bin/env python
# -*- coding=utf-8 -*-
# 包装配置登录文件的类方法

import os
import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(self.config_path, 'ssh_login.cfg')

    def write_login_config(self, section_name, user, password, default_dir=os.path.dirname(os.path.abspath(__file__)) + '/upload'):
        """将密码写入section name为主机host的ip的配置文件中"""
        self.config[section_name] = {}
        self.config[section_name]['user'] = user
        self.config[section_name]['password'] = password
        self.config[section_name]['default_file_dir'] = default_dir
        with open(self.config_file_path, 'w') as f:
            self.config.write(f)

    def read_config(self, config_file_path, section_name):
        """读取配置文件获得用户密码，section为用户名"""
        self.config.read(config_file_path)
        sections = self.config.sections()
        if section_name in sections:
            return self.config[section_name]
        else:
            return None


def main():
    config = Config()
    path = config.config_file_path
    config.write_login_config('192.168.23.129', 'root', '2587539619')
    content = config.read_config(path, '192.168.23.129')
    # print(dict(content)['user'])
if __name__ == '__main__':
    main()
