

'''
使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
需考虑网络异常、超时等问题，增加必要的异常处理。
因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。


-n：指定并发数量。
-f ping：进行 ping 测试
-f tcp：进行 tcp 端口开放、关闭测试。
-ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
-w：扫描结果进行保存。
'''

import os
import platform
import re
import telnetlib
import argparse

def isWindows():
    if platform.system() == "Windows":
        return True
    else:
        return False


def pingIP(ip):
    # ip = '192.168.47.2'
    ping = os.popen("ping {} -n 1".format(ip)).read()
    pingRes = re.compile(r'来自..+', re.M).findall(ping)
    # print(pingRes)
    if len(pingRes) >= 1:
        print(pingRes[0])
        return True
    else:
        print('{} ping 不通'.format(ip))

def get_ip_status(ip,port):
    server = telnetlib.Telnet()      # 创建一个Telnet对象
    try:
        server.open(ip,port)         # 利用Telnet对象的open方法进行tcp链接
        print('{0} port {1} is open'.format(ip, port))
        return '{0} port {1} is open'.format(ip, port)
    except Exception as err:
        print('{0} port {1} is not open'.format(ip,port))
        return '{0} port {1} is open'.format(ip, port)
    finally:
        server.close()


def getIPList(ipstr):
    iplist = []
    if '-' in ipstr:
        spotindex = ipstr.split('-')[0].rindex('.')
        ipseg = ipstr.split('-')[0][:spotindex]

        ipstart = ipstr.split('-')[0].split('.')[-1]
        ipend = ipstr.split('-')[1].split('.')[-1]
        for i in range(int(ipstart), int(ipend)+1):
            iplist.append(ipseg + '.' + str(i))
    else:
        iplist.append(ipstr)

    return iplist


def getPortList(portstr):
    portlist = []
    # print('$'*20)
    # print(portstr.split(','))
    for port in portstr.split(','):
        portlist.append(port.strip())

    return portlist

def save2file(filename):

    if os.path.isfile(filename):
        os.remove(filename)
    return open(filename,'w+')


def args(parser):

    # if parser.outfile:
    #     global outfile
    #     outfile = save2file(parser.outfile)

    if parser.type == 'ping' and parser.outfile:
        outfile = save2file(parser.outfile)
        for ip in getIPList(parser.ipstr):
            outfile.write(pingIP(ip) + '\n')
        outfile.close()
    elif parser.type == 'ping':
        for ip in getIPList(parser.ipstr):
            pingIP(ip)

    if parser.type == 'tcp' and parser.outfile:
        outfile = save2file(parser.outfile)
        if not parser.ports:
            raise r"请指定扫描端口"
        for ip in getIPList(parser.ipstr):
            # print(getIPList(parser.ports))
            for port in getPortList(parser.ports):
                # print(port)
                outfile.write(get_ip_status(ip,port) + '\n')

        outfile.close()
    elif parser.type == 'tcp':
        if not parser.ports:
            raise r"请指定扫描端口"
        for ip in getIPList(parser.ipstr):
            # print(getIPList(parser.ports))
            for port in getPortList(parser.ports):
                # print(port)
                get_ip_status(ip,port)



if __name__ == '__main__':
    # get_ip_status('192.168.47.165','3306')
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest='threadNum', default='1',help='指定线程数')
    parser.add_argument('-f', dest='type',choices=['ping','tcp'], default='ping',help='直接扫码的方式 ping/tcp')
    parser.add_argument('-ip' ,required=True, dest='ipstr',help='指定ip地址 eg -ip 1.1.1.1 or -ip 1.1.1.1-1.1.1.6')
    parser.add_argument('--tcpports','-tp' , dest='ports',help='指定扫描的端口,eg -tp 3306,22')
    parser.add_argument('-w',dest='outfile',help='指定结果保存的位置, eg -w out.txt')

    ops = parser.parse_args()
    # print(getIPList())
    # print(ops.type)
    args(ops)