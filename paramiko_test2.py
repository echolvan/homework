# 使用paramiko进行ssh连接，并执行命令行操作

import paramiko
from paramiko import SSHClient, SSHException

HOST = '192.168.23.129'
PASSWORD = '2587539619'
USER = 'root'

# paramiko.util.log_to_file('ssh_link_remote_server.log')


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
        except Exception as e:
            print(e)
            self.client = None

    def send_cmd(self, cmd):
        """发送命令取得返回值"""
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            print(stdout, stderr)
            return stdout
        except SSHException as e:
            print(e)

    def close(self):
        self.client.close()


def connect(host, password, user):
    """连接服务器"""
    # client.load_system_host_keys()   # 这里是用公钥和私钥登录的
    # client.connect()
    # stdin, stdout, stderr = client.exec_command('')
    client = ''
    try:
        client = SSHClient()
        # 我们第一次连接时会去核实host它会去找known_host_key的这个文件，没有按如下处理
        client.set_missing_host_key_policy(AcceptPolicy())
        # 我们hostkey不在时的规定:set policy to use when connecting to servers without a known_host_key,然后我们另起炉灶
        client.connect(hostname=HOST, username=USER, password=PASSWORD, timeout=10)
    except Exception as e:
        print(e)
    print(client)
    return client


def send_cmd(client, cmd):
    """发送命令取得返回值"""
    try:
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdout, stderr)
        return stdout
    except SSHException as e:
        print(e)


def upload(client, local_file_path, remote_file_path):
    """put local file to remote server"""
    try:
        ret = {'status': 0, 'msg': 'ok'}
        if client:
            ftp_client = client.open_sftp()
            ftp_client.put(local_file_path, remote_file_path)
            print('上传成功')
            ftp_client.close()

        else:
            ret['status'] = 1
            ret['msg'] = 'error'
    except Exception as e:
        ret['status'] = 1
        ret['msg'] = e
    return ret


def download(client, remote_file_path, local_file_path):
    """get file from remote server"""
    try:
        ret = {'status': 0, 'msg': 'ok'}
        if client:
            ftp_client = client.open_sftp()
            ftp_client.get(remote_file_path, local_file_path)
            print('下载成功')
            ftp_client.close()

        else:
            ret['status'] = 1
            ret['msg'] = 'error'
    except Exception as e:
        ret['status'] = 1
        ret['msg'] = e
    return ret


def main():
    client = connect(host=HOST, password=PASSWORD, user=USER)
    if client:
        while True:
            print('请输入shell命令，[upload]-上传 [download]-下载 [q]-退出')
            cmd = input('>>>')
            if cmd == 'q':
                break
            elif cmd == 'upload':
                local_file_path = input('local_file_path：')
                remote_file_path = input('remote_file_path：')
                result = upload(client, local_file_path, remote_file_path)
                print(result)
                continue
            elif cmd == 'download':
                remote_file_path = input('remote_file_path')
                local_file_path = input('local_file_path')
                result = download(client, remote_file_path, local_file_path)
                print(result)
                continue
            stdout = send_cmd(client, cmd)
            print(stdout.read().decode())
        client.close()


def test():
    ssh = MySSH('192.168.23.129', '2587539619', 'root')
    print(ssh.send_cmd('df -h').read().decode())

if __name__ == '__main__':
    test()