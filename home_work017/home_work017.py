# ### 4.2 web 服务程序实现
#   1. 主要功能 ：
#      【1】 接收客户端（浏览器）请求
#      【2】 解析客户端发送的请求
#      【3】 根据请求组织数据内容
#      【4】 将数据内容形成http响应格式返回给浏览器
#   2. 特点 ：
#      【1】 采用IO并发，可以满足多个客户端同时发起请求情况
#      【2】 通过类接口形式进行功能封装
#      【3】 做基本的请求解析，根据具体请求返回具体内容，同时处理客户端的非网页请求行为

"""/usr/bin/python3.6 /home/tarena/cuiyue/month02/teacher_code/day17/home_work017/home_works.py
客户端('127.0.0.1', 52534)已经连接上
GET / HTTP/1.1
Host: 127.0.0.1:8888"""
from select import *
from socket import *


class Webserver():
    def __init__(self, addr=("0.0.0.0", 8888), html_addr=None):
        self.addr = addr
        self.html_addr = html_addr
        self.socket()
        self.bind()
        self.c_ep()

    def start(self):
        self.ep.register(self.s,EPOLLIN)
        self.s.listen(10)
        while True:

            events = self.ep.poll()   #等待处理IO事件产生
            for fd,event in events:
                if fd ==self.s.fileno():
                    conn,addr = self.dict_s[fd].accept()
                    print("%s已经链接上"%addr)




    def socket(self):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.setblocking()
        self.dict_s=[]
        self.dict_s[self.s.fileno()] = self.s   #fileno 获取文件描述符的函数
    def bind(self):
        self.s.bind(self.addr)

    def c_ep(self):
        self.ep = epoll()


if __name__ == '__main__':
    httpd = Webserver(("127.0.0.0", 8888), html_addr="../static")
    httpd.start()
