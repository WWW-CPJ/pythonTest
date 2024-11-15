"""
http://t.csdnimg.cn/wnGU2
"""
# import socket
# 查询IP
# 利用Python中的socket模块的gethostbyname函数能够实现解析域名 IP 地址的功能

# def ip_check(url):
#     ip = socket.gethostbyname("www.ycpai.cn")
#     print(ip)
    
# print(socket.gethostbyname("www.baidu.come"))



import whois

def ip_check(url):
    ip = whois.whois("www.baidu.com")