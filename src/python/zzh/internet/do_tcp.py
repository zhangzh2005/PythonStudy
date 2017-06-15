'''
Created on 2017/06/09

@author: BAB1700057
'''
import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('www.sina.com.cn',80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    
    s.close()
    
    # 用第一个遇到的‘\r\n\r\n’来分割
    header,html= data.split(b'\r\n\r\n', 1)
    
    print(header.decode('utf-8'))
    
    with open('sina.html','wb') as f:
        f.write(html)
    
    
    