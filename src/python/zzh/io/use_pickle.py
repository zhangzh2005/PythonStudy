'''
Created on 2017/06/01

@author: BAB1700057
'''
import pickle

if __name__ == '__main__':
    d = dict(name='Bob',age=20,score=80)
    pickle.dumps(d)
    
    f = open('./test.txt','wb')
    pickle.dump(d,f)
    f.close()
    
    with open('./test.txt','rb') as f:
#     f = open('./test.txt','rb')
        d = pickle.load(f)
#     f.close()
        print(d)