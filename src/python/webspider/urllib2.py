'''
Created on 2017/06/15

@author: BAB1700057
'''
import urllib
import urllib.request

if __name__ == '__main__':
    response = urllib.request.urlopen('https://www.baidu.com')
    print(response.info