'''
Created on 2017/06/01

@author: BAB1700057
'''
from io import BytesIO

if __name__ == '__main__':
    f = BytesIO()
    f.write('聞く'.encode(encoding='utf_8', errors='strict'))
    print(f.getvalue())
    
    
    f = BytesIO(b'\xe8\x81\x9e\xe3\x81\x8f')
    print(f.read())
    
            

    