'''
Created on 2017/06/01

@author: BAB1700057
'''
import subprocess

if __name__ == '__main__':
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup','www.python.org'])
    print('Exit code:', r)
