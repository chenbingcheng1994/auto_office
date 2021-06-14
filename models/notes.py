import os
import time
from config import *

"""
Python从‘Notes.app’获取数据，并做数据处理

"""
def open_notes():

    # 获取'God Witnesses'下所有notes的创建时间,并做格式化处理

    # os.system(notes_created_date_command)-无需返回值可用该函数
    resp = os.popen(notes_created_date_command).readlines()
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





    # for i in notes_date_list:
    #     print(i.lstrip())



    # time.sleep(3)


    # os.system('pkill -x Notes')


if __name__ == "__main__":
    open_notes()
    # print(resp)


