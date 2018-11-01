#实现了将一个文档中的每一行内容分类，并按类将其转化为csv文件，统计了保存一个文档的时间
import re#引入正则表达式
import csv#引入csv
import time
file_name='e:/huawei/12/cnki.cdn.bcebos.com.2018_09_12_20_00'
file_object=open(file_name)
a=True
t1=time.time()
p=r'(.*) - - (.*) (\[.*\]) (.*) "(.*)" (.*) (.*) (.*) "(.*)" "(.*)" "(.*)" "(.*)" (.*) "(.*)" (.*)'
count=0
while a:
    line=file_object.readline()#逐行读取
    line_m=re.match(p,line,re.M | re.I)
    print(line_m)
    if line_m==None:
        a=0
    else:
        a=1
        row = [(item for item in line_m.groups())]#将正则表达式匹配的group分离
        f=open('data_test_0.csv', 'a+', newline='')#'a'表示附加读写方式打开
        f_csv = csv.writer(f)
        f_csv.writerows(row)#将文件以csv格式写入
    count+=1
t2=time.time()
print('保存的行数：',count)
print('保存所需时间：',t2-t1)#转换文件所需的时间
