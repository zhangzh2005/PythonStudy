'''
Created on 2017/05/31

@author: BAB1700057
'''
import unittest

from python.zzh.helloWorld import HelloWorld


class Test(unittest.TestCase):


    def testHelloWorld(self):
        h = HelloWorld('zzh')
        self.assertEqual(h.get_name(),'zzh')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHelloWorld']
    unittest.main()