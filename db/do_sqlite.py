# -*- coding: utf-8 -*-
# @Time : 2022/11/27 9:57
# @Author :liuw
# @File : do_sqlite.py
# @Software: PyCharm
# Sqlite是一种嵌入式数据库，本身是使用C 写的，体积很小内置在python当中

# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 将会打印输出<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'2\', \'Michael\')')
# <sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
cursor.rowcount
# 打印输出1
# 提交事务:
conn.commit()
# 关闭Cursor:
cursor.close()
# 关闭Connection:
conn.close()

# 使用查询语句
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# 一个练习 请编写函数，在Sqlite中根据分数段查找指定的名字：

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('select name from user where score >=? and score<=? order by score', (low, high,))
        values = cursor.fetchall()
        print(values)  # 返回的是包含不同人名的列表 每个人名又是一个元组 [('Bart',), ('Lisa',)]
        name_list = [v[0] for v in values]  # 取元组里第一个元素，舍弃,
        print(name_list)  # ['Bart', 'Lisa']
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return name_list


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
