'''
Created on 2017/06/09

@author: BAB1700057
'''
from PIL import Image

if __name__ == '__main__':
    im = Image.open('test.jpg')
    
    w,h = im.size
    
    print('Original image size : %sx%s' % (w,h))
    
    im.thumbnail((w//2,h//2))
    
    print('Resize image to : %sx%s' % (w//2,h//2))
    
    im.save('thumbnail.jpg','jpeg')
    