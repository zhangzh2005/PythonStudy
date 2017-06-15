'''
Created on 2017/06/09

@author: BAB1700057
'''
import socket

if __name__ == '__main__':
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9999))
    
    print(s.recv(1024).decode('utf-8'))
    
    for data in [b'Michel',b'andy',b'Can']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    
    s.send(b'exit')
    s.close()