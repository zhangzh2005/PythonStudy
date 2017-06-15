'''
Created on 2017/06/09

@author: BAB1700057
'''
import socket,threading,time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % (sock,addr))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
        
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    s.listen(5)
    print('Waiting for connection...')
    
    while True:
        sock,addr = s.accept()
        t = threading.Thread(target = tcplink, args=(sock,addr))
        t.start()
        