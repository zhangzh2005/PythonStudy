'''
Created on 2017/06/12

@author: BAB1700057
'''
import numpy as nper
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
    df.sort_values(by, axis, ascending, inplace, kind, na_position)