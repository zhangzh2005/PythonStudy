'''
Created on 2017/06/09

@author: BAB1700057
'''
import sqlite3

def createTbl():
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    try:
        
        cursor.execute('create table user (id varchar(20) primary key, name verchar(20))')
        cursor.execute('insert into user(id,name) values (\'1\',\'Andy\')')
        conn.commit()

    finally:
        cursor.close()
        conn.close()
    
if __name__ == '__main__':
    
    # createTbl()
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where id=?',('1',))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()

    
    