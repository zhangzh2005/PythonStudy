'''
Created on 2017/06/01

@author: BAB1700057
'''
import json

    
class Student(object):
    def __init__(self,name,age,score):
        self._name = name
        self._age = age
        self._score = score
        
        

def dict2Student(d):
    return Student(d['name'],d['age'],d['score'])


if __name__ == '__main__':
    d = dict(name='Bob',age=20,score=80)
    s = json.dumps(d)
    print(s)
    
    json_str = '{"age":20,"score":88,"name":"Andy"}'
    s = json.loads(json_str)
    print(s)
    
    s = Student("Fla",30,100)
    
    print(dir(s))
    
    print(json.dumps(s,default=lambda obj:obj.__dict__))
    
    s = json.loads(json_str,object_hook=dict2Student)
    print(s)
    
    

        