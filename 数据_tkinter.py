import tkinter as tk
import csv
import time
import re

window=tk.Tk()
window.title('生成CSV文件：')
window.geometry('500x600')
canvas = tk.Canvas(window, height=200, width=500)#创建画布
image_file = tk.PhotoImage(file='welcome.gif')#加载图片文件
image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
canvas.pack(side='top')#放置画布（为上端）

var1=tk.StringVar()
var2=tk.StringVar()
var4=tk.StringVar()
var1.set('请输入原始文件地址：')
l=tk.Label(window,
           textvariable=var1,
           bg='white',
           font=('Aria',15),
           width=30,
           height=3)
l.pack()

e1=tk.Entry(window)
e1.pack()

var2.set('请输入保存文件名称及格式：')
l=tk.Label(window,
           textvariable=var2,
           bg='white',
           font=('Aria',15),
           width=30,
           height=3)
l.pack()

e2=tk.Entry(window)
e2.pack()


on_hit=False
def hit_me():
    address = str(e1.get())
    name = str(e2.get())
    global on_hit
    if on_hit==False:
        on_hit=True
        file_object = open(address)
        a = True
        t1 = time.time()
        p = r'(.*) - - (.*) (\[.*\]) (.*) "(.*)" (.*) (.*) (.*) "(.*)" "(.*)" "(.*)" "(.*)" (.*) "(.*)" (.*)'
        count=0
        while a:
            line = file_object.readline()
            line_m = re.match(p, line, re.M | re.I)
            print(line_m)
            if line_m == None:
                a = 0
                var4.set('已经转换完成，转换%s \n 所用时间:%s' % (count,t))
            else:
                a = 1
                row = [(item for item in line_m.groups())]
                f = open(name, 'a+', newline='')
                f_csv = csv.writer(f)
                f_csv.writerows(row)
                count+=1
                var4.set('转换了%s 行' % count)
            t2=time.time()
            t=t2-t1

    else:
        on_hit=False
        b.config(text='重复添加')

l1 = tk.Label(window,
           textvariable=var4,
           bg='white',
           font=('Aria',15),
           width=30,
           height=3)
l1.pack()

b=tk.Button(window,text='确认',font=('Aria',15),width=30,bg='green',height=3,command=hit_me)
b.pack()
tk.mainloop()