import paramiko
import os,sys
# 使用用户名密码登陆
def remoteLoginWithUP(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("localhost",22,'NikoBelic','Lixiwei000')
    stdin,stdout,stderr = ssh.exec_command(cmd)
    for line in stdout.readlines():
        print(line.strip())
    ssh.close()

'''
SSH免密登陆原理
    1.A将自己的公钥事先发送给B
    2.A向B发送登陆请求
    3.B接收到请求以后,使用A提供的pub对一串随机数进行加密,发送给A
    4.A收到B的密文后尝试使用pri解密,将解密结果发送给B,如果B判断A解密成功,则A成功登陆B,A与B之间可以进行明文通信了
    5.C如果截获了B给A的密文,是解不开的,所以

'''
# 使用公钥私钥登陆
def remoteLoginWithKey(cmd):
    privateKeyPath = "/Users/lixiwei-mac/.ssh/id_rsa"
    key = paramiko.RSAKey.from_private_key_file(privateKeyPath)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('localhost',22,username="NikoBelic",pkey=key)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    for line in stdout.readlines():
        print(line.strip())
    ssh.close()

# 文件上传下载
def ftpTest():
    t = paramiko.Transport(('localhost',22))
    t.connect(username='NikoBelic',password='Lixiwei000')
    sftp = paramiko.SFTPClient.from_transport(t)
    # upload
    sftp.put("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day6/CloudFS/README.md","/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day6/LocalFS/README.md")
    # download
    sftp.get("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day6/CloudFS/README.md","/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day6/LocalFS/test.md")
    t.close()

if __name__ == "__main__":

    remoteLoginWithKey("ls /")