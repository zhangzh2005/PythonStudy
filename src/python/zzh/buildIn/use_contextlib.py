'''
Created on 2017/06/02

@author: BAB1700057
'''

from contextlib import contextmanager,closing
from urllib.request import urlopen

class Query(object):
    def __init__(self,name):
        self._name = name
        
    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    
    def query(self):
        print('Query infor about %s...' % self._name)
        
        
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query3 info about %s...' % self.name)
    

if __name__ == "__main__":
    
    # __enter__ __exit__實現上下文
    with Query('Bob') as q:
        q.query()
    
    # contextmanager實現上下文
    @contextmanager
    def create_query2(name):
        print('Begin query2...')
        q = Query2(name)
        yield q
        print('End query2')
        
    with create_query2('Alice') as q:
        q.query()
        
    # 實現某段代码执行前后自动执行特定代码
    @contextmanager
    def tag(name):
        print("<%s>" % name)
        yield
        print("</%s>" % name)
    
    with tag("h1"):
        print('hello')
        print('world')
        
    # closing實現With
    with closing(urlopen('http://www.baidu.com')) as page:
        for line in page:
            print(line)
        
    
        
        
        
    
        
