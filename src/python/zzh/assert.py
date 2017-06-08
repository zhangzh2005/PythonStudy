'''
Created on 2017/06/02

@author: BAB1700057
'''
def foo(s):
    n = int(s)
    assert n != 0, 'NG!'
    print('OK')
    return 10 / n

if __name__ == '__main__':
    foo(1)