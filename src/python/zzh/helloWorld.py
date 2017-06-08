'''
Created on 2017/05/31

@author: BAB1700057
'''

class HelloWorld(object):
    '''
    This is the first class
    '''
    def __init__(self,para = 'world'):
        self._name = para

    
    def set_name(self,name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def say(self):
        print('hello' , self._name)
        
