import pymysql
import logging
from config import *

"""
1.Mysql数据库基本操作；
2.向Mysql插入从'Note.app'获取的数据

"""
class Database():

    def __init__(self, host, user, password, database, table_name,*args, **kwargs):

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table_name = table_name

    # 创建数据库
    def Create_DB(host,username,password,database):
        db = pymysql.connect(host=host,user=username,password=password)
        cursor = db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS %s"%database
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute("SELECT VERSION()") 
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone() 
        print ("Database version : %s " % data)
        # 关闭游标、数据库
        cursor.close()
        db.close() 

    # 创建数据库表格
    def Create_Table(host,username,password,database,table_name):
        db = pymysql.connect(host=host,user=username,password=password,database=database)
        cursor = db.cursor()
        # 查询当前进入的数据库
        sql =  ("SELECT DATABASE();")
        cursor.execute(sql)
        data = cursor.fetchall()
        print("Now, we are in database : %s " %data)
        # 创建数据库表
        print(love_sql)
        cursor.execute(love_sql)
        print(cursor.fetchall())
        cursor.execute('alter table %s AUTO_INCREMENT=1'%table_name)
        # 关闭游标、数据库
        cursor.close()
        db.close()
    
    # 向数据库里面插入数据
    def Insert_Data(host,username,password,database,table_name,**kwargs):
        db = pymysql.connect(host=host,user=username,password=password,database=database)
        cursor = db.cursor()

        # 查询表格desc
        cursor.execute("desc %s;"%table_name)
        data = cursor.fetchall()
        print(data)
        print(len(data))

        insert_numb = len(data)
        # 需要插入的元素名称
        insert_varible = []
        # insert_sql构造'%s%s'字符串
        values_list = []
        # 过滤出数据库中自动生成的数据，最后要需要插入的元素为列表insert_varible中的元素
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 'auto_increment':
                    insert_numb = insert_numb - 1
                    need_no_insert = i
                    print(need_no_insert)
                else:
                    pass
            insert_varible.append(data[i][0])
        insert_varible.remove(data[need_no_insert][0])

        print(insert_numb)
        print(insert_varible[0])

        for i in range(int(insert_numb)):
            values_list.append('%s')
        print(values_list)

        # 生成插入数据库语句
        insert_sql = "INSERT INTO %s (%s) VALUES (%r,%s,%s,%s,%s,%s,%r,%r);"%(table_name,','.join(insert_varible),EXECUTING_TIME,DATETIME,LOCATION,WEATHER,TITLE,BODY,PICTURE,OTHERS)
        print(insert_sql)
        cursor.execute(insert_sql)
        print(cursor.fetchall())
        # 关闭游标、数据库
        db.commit()
        cursor.close()
        db.close()
    


if __name__ =='__main__':

    # 初始化
    EXECUTING_TIME = "2021-06-19"
    DATETIME = "'Monday 14 June 2021 at 17:24:23'"
    LOCATION = "'shenzhen'"
    WEATHER = "'sunny'"
    TITLE = "'我和奥林'"
    BODY = "'wearehappy'"
    PICTURE = '//Users//chenbingcheng'
    OTHERS = '//Users//chenbingcheng'

    # Database.Create_DB(host=host,username=username,password=password,database=database)
    #Database.Create_Table(host=host,username=username,password=password,database=database,table_name=table_name)
    Database.Insert_Data(host=host,username=username,password=password,database=database,table_name=table_name, \
                        EXECUTING_TIME=EXECUTING_TIME,DATETIME = DATETIME,LOCATION=LOCATION,WEATHER=WEATHER, \
                        TITLE=TITLE,BODY=BODY,PICTURE=PICTURE,OTHERS=OTHERS)

