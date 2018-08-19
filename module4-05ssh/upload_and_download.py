# !/usr/bin/env python
# -*- coding=utf-8 -*-
# 包装好的上传和下载函数

import logging
import os

import paramiko

from mylog import log

# log = my_logger('control_line.log', logging.DEBUG, 'control_line')


def upload(client, local_file_path, remote_file_path):
    """put local file to remote server"""
    try:
        ret = {'status': 0, 'msg': 'ok'}
        if client:
            ftp_client = client.open_sftp()
            ftp_client.put(local_file_path, remote_file_path)
            log.debug(f'{local_file_path}上传到远程服务器端{remote_file_path}')
            print('上传成功')
            ftp_client.close()

        else:
            ret['status'] = 1
            ret['msg'] = 'error'
            log.debug('上传文件至服务器的连接未建立成功')
    except Exception as e:
        ret['status'] = 1
        ret['msg'] = e
        log.debug(f'上传服务中出现错误：{e}')
    return ret


def download(client, remote_file_path, local_file_path):
    """get file from remote server"""
    try:
        ret = {'status': 0, 'msg': 'ok'}
        if client:
            ftp_client = client.open_sftp()
            ftp_client.get(remote_file_path, local_file_path)
            log.debug(f'远程服务器端文件{remote_file_path}下载到本地{local_file_path }')
            print('下载成功')
            ftp_client.close()

        else:
            ret['status'] = 1
            ret['msg'] = 'error'
            log.debug('下载服务的连接未建立成功')
    except Exception as e:
        ret['status'] = 1
        ret['msg'] = e
        log.debug(f'下载服务中出现错误：{e}')
    return ret


def upload_many(client):
    """批量上传，在upload目录的文件将全部被上传"""
    filedir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(filedir, 'upload')
    f = os.walk(filepath)
    for i in f:
        u_list = i[2]
        base_path = i[0]
    try:
        ret = {'status': 0, 'msg': 'ok'}
        if client:
            ftp_client = client.open_sftp()
            for local_file in u_list:
                local_file_path = os.path.join(base_path, local_file)
                remote_file_path = 'upload/' + local_file
                ftp_client.put(local_file_path, remote_file_path)
                log.debug(f'{local_file_path}上传到远程服务器端{remote_file_path}')
                print('上传成功')
            ftp_client.close()

        else:
            ret['status'] = 1
            ret['msg'] = 'error'
            log.debug('上传服务的连接未建立成功')
    except Exception as e:
        ret['status'] = 1
        ret['msg'] = e
        log.debug(f'上传服务中出现错误：{e}')
    return ret



def main():
    upload_many()

if __name__ == '__main__':
    main()