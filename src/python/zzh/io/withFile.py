'''
Created on 2017/06/01

@author: BAB1700057
'''

if __name__ == '__main__':
    '''
    try...finally
    
    try:
        f = open('./test.txt','r')
        print(f.read())
    finally:
        if f:
            f.close()
    '''
    
    '''
    with
    '''
    with open('./test.txt','w') as f:
        f.write('zzz')
        
        
    


