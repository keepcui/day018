from select import select
from socket import *

s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(3)
rlist = [s]
wlist = []
xlist = []
s.setblocking(False)   #设置称非阻塞的状态
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c ,addr = r.accept()    #等待客户端链接
            print("客户端%s已经连接上"%(addr,))
            rlist.append(c)
            c.setblocking(False)
        elif r is c:
            data = r.recv(4096)
            if not data :
                print("客户端已经断开链接")
                r.close()
                rlist.remove(r)
            print(data.decode())




