'''
Created on 2017/06/02

@author: BAB1700057
'''
import re
from _sre import MAXGROUPS


if __name__ == '__main__':
    print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
    print(re.match(r'^\d{3}-\d{3,8}','010 12345'))
    
    test = '010-12345'
    if re.match(r'^\d{3}\-\d{3,8}$',test):
        print('ok')
    else:
        print('failed')
    
    # 用固定的字符切分
    print('a,b   c'.split(' '))
    
    # 用正则表达式切分
    print(re.split(r'\s+','a b   c'))
    print(re.split(r'[\s\,]+','a,b   c'))
    print(re.split(r'[\s\,\;]+','a,b;;;   c'))
    
    # 定义group并提取分组
    m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    
    # 贪婪匹配
    g = re.match(r'^(\d+)(0*)$','1020000').groups
    print(g())
    
    g = re.match(r'^(\d+?)(0*)$','1020000').groups
    print(g())
    
    # 编译正则表达式
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    g = re_telephone.match('010-55555').groups()
    print(g)
    