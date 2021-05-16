import pymysql
import logging
# from config import *

"""
Mysql数据库基本操作

"""
class Database():

    def __init__(self, host, user, password, database, *args, **kwargs):

        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 连接数据库
    def Connect_Mysql(self):
        db = pymysql.connect(host=host,user=username,password=password,database=datebase)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

    # 创建数据库列表
    def Create_Table(self, table_name):
        self.table_name = table_name
        sql = "CREATE TABLE IF NOT EXISTS `%s`( \
        `DATE` DATE, \
        `INCOME` VARCHAR(100) NOT NULL \
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;"%table_name
        cursor.execute(sql)






if __name__ =='__main__':

    #打开数据库连接
    db = pymysql.connect(host=host,user=username,password=password,database=datebase)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
 
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("CREATE DATABASE CHEN;")
 
    # 使用预处理语句创建表
    #sql = """CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT )"""
 
    #cursor.execute(sql)
 
    # 关闭数据库连接
    db.close()