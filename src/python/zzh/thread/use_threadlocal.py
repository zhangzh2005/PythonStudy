'''
Created on 2017/06/01

@author: BAB1700057
'''
import threading

def process_student(student):
    std = student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))
    
    
def process_thread(name):
    for i in range(1000):
        process_student(name)

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
    t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    