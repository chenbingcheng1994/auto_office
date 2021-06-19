
a=len('我说的马放南山的烦恼')
print(a)
# sql = "insert into t_dc_result(fid,fdate,fproduct_id,fcost_time,fstatus,flog_content,fbus_type,fbus_name,fpmoney,fomoney)" \
#                   " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# print(sql)
import time
 
localtime = time.asctime( time.localtime(time.time()) )
print('本地时间为: %r'%localtime)
print(time.strftime("%Y-%m-%d", time.localtime()))