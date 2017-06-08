'''
Created on 2017/06/02

@author: BAB1700057
'''
import base64
import unittest

def safe_base64_decode(s):
    number_of_equal = len(s)%4
    if isinstance(s,bytes):
        code = s + b'='*number_of_equal
    elif isinstance(s,str):
        code = s + '='*number_of_equal 
    return base64.urlsafe_b64decode(code)
    
class Test(unittest.TestCase):
    def testbase64(self):
        assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
        assert b'abcd' == safe_base64_decode(b'YWJjZA')
        print('Pass')
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()