'''
Created on 2017/06/01

@author: BAB1700057
'''

from io import StringIO

if __name__ == '__main__':
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world')
#     print(f.getvalue())
    
    f = StringIO('fdsf\neeee\ntttt\nsssss')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())
