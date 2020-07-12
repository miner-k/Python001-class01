
# ipstr='192.168.0.1-192.168.0.100'
#
#
# spotindex = ipstr.split('-')[0].rindex('.')
# ipseg = ipstr.split('-')[0][:spotindex]
#
# ipstart = ipstr.split('-')[0].split('.')[-1]
# ipend = ipstr.split('-')[1].split('.')[-1]
# for i in range(int(ipstart),int(ipend)):
#     print(ipseg + '.' +str(i))

# portstr = "22,21, 3306 "
# print(portstr.split(','))
# portlist = []
# for port in portstr.split(','):
#     portlist.append(port.strip())
#
# print(portlist)
# def o2f():
#     # with open('1.txt','w+') as f:
#     #     return f
#     return  open("1.txt",'w+')
#
# newf = o2f()
# newf.write("hello")
# newf.write("hello")
# newf.write("hello")
# newf.write("hello")
# newf.writelines("hello world")
# newf.writelines("hello world")

import os
print(os.getppid())