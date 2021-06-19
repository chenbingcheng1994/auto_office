import os
import time
from config import *
from bs4 import BeautifulSoup

"""
从‘Notes.app’获取数据并处理
1.获取创建时间；
2.获取Notes.Name;
3.获取Notes.Body;
"""

class Notes():

    def __init__(self,notes_command):
        self.notes_command = notes_command

    def get_created_time(self):

        # 获取notes的创建时间,并做格式化处理
        # os.system(notes_command)-无需返回值可用该函数
        resp = os.popen(self.notes_command).readlines()
        print(resp)
        notes_date_list = resp[0].replace('\n','').replace('date ','').split(',')
        print(notes_date_list)
        print(int(len(notes_date_list)/2))
        notes_created_datetime= []
        for i in range(0,int(len(notes_date_list)/2)):
            notes_date = notes_date_list[2*i] + notes_date_list[2*i+1]
            notes_created_datetime.append(notes_date.lstrip())
        print("########")
        print(notes_created_datetime)       
        return  notes_created_datetime

    def get_notes_name(self):

        # 获取notes名称
        resp = os.popen(self.notes_command).readlines()
        print(resp)
        notes_name_list = resp[0].split(',')
        print(notes_name_list)
        notes_created_name = []
        for i in range(len(notes_name_list)):
            notes_name = str(notes_name_list[i].lstrip())
            notes_created_name.append(notes_name)
        # 写入文件
            filename = 'test_text.txt'
            with open(filename, 'a') as file_object:
                file_object.write(notes_created_name[i]+"\n")

        print("########")
        # print(notes_created_name)


        for i in range(len(notes_created_name)):
            print(notes_created_name[i]+"#len"+str(len(notes_created_name[i])))
        return notes_created_name

    def get_notes_body(self):

        ## 获取“God Witnesses”目录下所有笔记的的body
        ## 并且将其并凑成一个str类型的数据:notes_body_str1
        resp = os.popen(self.notes_command).readlines()
        print('######'+'resp的长度为：%d'%(len(resp)))
        notes_body_str = []
        for i in range(len(resp)):
            notes_body_str.append(resp[i])
        notes_body_str1 = ''.join(notes_body_str)

        ## 将notes_body_str1，通过头部(', <div>')标识做切割成列表notes_body_list，分成自然一个一个笔记
        notes_body_list = notes_body_str1.split(', <div>')
        print('当前God_Witnesses中笔记的个数为：%d'%len(notes_body_list))

        ## 将列表元素，写入note_body.txt文件中
        filename = 'note_body.txt'
        with open(filename, 'w') as file_object:
            for i in range(len(notes_body_list)):
                file_object.write(notes_body_list[i])

        ## 对列表notes_body_list，使用Beautifulsoup4库进行html元素提取
        notes_title = []
        for i in range(len(notes_body_list)):
            bs = BeautifulSoup(notes_body_list[i],"html.parser")
            title = ''
            for item in bs.find_all("h1"): 
                a = item.get_text()
                title = title + a
                # print(type(a))
                # print(a)        
            print(title)
            notes_title.append(str(title))
        print(notes_title)


        # for item in bs.find_all("h1"): 
        #     notes_body = []
        #     notes_body = notes_body.append(item.get_text())
        # print(notes_body)



    # time.sleep(3)


    # os.system('pkill -x Notes')


if __name__ == "__main__":
    a = Notes(notes_body_command).get_notes_body()
    # print(Notes(notes_body_command).get_notes_name())


