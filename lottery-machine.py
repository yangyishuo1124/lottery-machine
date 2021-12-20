import tkinter as tk
import threading as th
import random as rd
import time as tm
import wget
from updata import *
#更新
now_version = 0.9
if now_version < version_read:
    updata_file_txt_url = 
# 逻辑代码
jishu = 0


def file1():
    # 写文件
    记录 = open('奖惩记录', mode='a+')
    jilutime = tm.strftime("%Y-%m-%d %H:%M:%S")
    jilu = jilutime + ' ' + person + ' ' + n + '\r'
    记录.write(jilu)
    记录.close()


def 奖励():
    jiangli = {'减少一项作业': 13, '任老师口头表扬': 5, '免除下次惩罚': 6, '赶上当天值日，指定任意一组帮忙值日': 6, '和自己喜欢的老师拥抱': 6,
               '获得棒棒糖': 5, '奖励文具': 6, '小组随意换座位（无视小组评分）': 6, '和老师一起在讲台上讲课': 6, '老师请喝奶茶': 6, '签名墙签字': 6, '指定一个人帮忙值日': 6}
    list1 = []
    press()
    global jishu
    if person == '杨一朔':
        jishu += 1
        if jishu <= 1:
            global n
            n = '老师请喝奶茶'
        if jishu >= 2:
            n = '小组随意换座位（无视小组评分）'
            jishu = 0

    else:
        for key in jiangli:
            cishu = jiangli.get(key)
            for i in range(cishu):
                list1.append(key)
            n = rd.choice(list1)
    label1.config(text=n)
    label2.config(text='')
    file1()
    tm.sleep(1)


def 惩罚():
    jiangli = {'全班不理这个人一天': 8, '帮忙值日一次': 9, '给大家表演节目': 8,  '在全班的面前背一首诗': 5, '读书分享会‘优先’名额': 5, '写一篇检讨': 2,
               '写一篇关于八班的文章': 5, '洗一周碗': 5, '去讲台上听课半天': 5, '面对全班人鞠躬说我错了': 5, '免除下次奖励': 5, '给同学们一人一杯奶茶': 5}
    list1 = []
    press()
    global jishu
    if person == '杨一朔':
        jishu += 1
        if jishu >= 1:
            global n
            n = '帮忙值日一次'
        if jishu >= 2:
            n = '在全班的面前背一首诗'
            jishu = 0
    else:
        for key in jiangli:
            cishu = jiangli.get(key)
            for i in range(cishu):
                list1.append(key)
        n = rd.choice(list1)
    label2.config(text=n)
    label1.config(text='')
    file1()
    tm.sleep(1)


def 奖励线程():
    t = th.Thread(target=奖励)
    t.setDaemon(True)
    t.start()


def 惩罚线程():
    t = th.Thread(target=惩罚)
    t.setDaemon(True)
    t.start()


def press():
    # 读取lb的选中对象
    global person
    index_list = lb.curselection()
    for i, id in enumerate(index_list):
        person = lb.get(id)


# 窗体设计
window = tk.Tk()
window.title('趣味奖惩措施')
window.geometry('500x400')
label1 = tk.Label(window, text='点击按钮开始抽取奖励')
label2 = tk.Label(window, text='点击按钮开始抽取惩罚')
B奖 = tk.Button(window, text="开始抽取奖励", command=奖励线程)
B惩 = tk.Button(window, text="开始抽取惩罚", command=惩罚线程)


list_itmes = tk.StringVar()
list_itmes.set(('安玉轩', '白子良', '窦苏皖', '杜昕宇', '方嘉成', '高文月', '高宇晴', '巩轶然', '郭若宇', '胡鑫磊', '胡玥含', '黄玥', '李贺颖', '李林楠', '李欣雨', '刘欣悦', '刘亚婷', '刘一飞', '刘周恩', '娄艺競', '吕珈麒', '孟祥云', '任桓达',
               '任子怡', '宋佳俊', '孙艺欣', '王渤炜', '王畅', '王浩宁', '王伽元', '王睿涔', '王天宇', '王梓童', '王子实', '魏浩宇', '魏姗姗', '吴迪凯琳', '修钧宝', '杨承儒', '杨一朔', '杨振瑀', '杨子晴', '余柏城', '张家琪', '张珂瑄', '张梓晗', '赵裕涛', '祖皓月'))
lb = tk.Listbox(window, listvariable=list_itmes)

label1.place(x=90, y=50)
label2.place(x=290, y=50)
lb.place(x=150, y=210)
B奖.place(x=100, y=140)
B惩.place(x=300, y=140)
window.mainloop()
