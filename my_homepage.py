import streamlit as sl
from PIL import Image
import json
import getpass
#python -m streamlit run 文件路径
#ctrl + c
import datetime
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
time = str(datetime.datetime.now())
page = sl.sidebar.radio('问卷星_我的网络根据地',["问卷设计(试运行)","问卷数据下载(试运行)","问卷数据API接口使用说明","兴趣推荐","图片处理工具","智慧词典",'留言板',"退出网页"])
text = """
    平台名称：问卷星_我的网络根据地\n
    用户：everyone\n
    主题：问卷收集\n
    增加功能：问卷设计/网站增加API数据接口，便于使用代码获取问卷数据。\n
"""
code = """
    print("Hello World!")
"""
username = getpass.getuser()

registerFont(TTFont("simhei","simhei.ttf"))

Temp = ["","",[]]
with open("information.json",'w') as f:
    json.dump(Temp,f)
    
with open("words_space.txt",'r',encoding='utf-8') as f:
    words_lists = f.read().split("\n")
for i in range(len(words_lists)):
    words_lists[i] = words_lists[i].split('#')
words_dicts = {} 

for i in words_lists:
    words_dicts[i[1]] = i[2]

def home_hobby():
    sl.title(':blue[欢迎！Welcome]')
    sl.write(text)
    sl.title(':blue[页面当前代码]')
    sl.code(code,language="python")
    sl.image('振兴中华.jpg')

def img_change(img,rc=0,gc=1,bc=2):
    w,h = img.size
    img_array = img.load()
    for x in range(w):
        for y in range(h):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img


def home_fanyi():
    sl.title("智慧词典")
    word = sl.text_input("请输入要查询的单词：")
    if word:
        if word in words_dicts:
            sl.code(words_dicts[word],language="python")
        else:
            sl.code(code,language="python")
    
        with open("cnt_json.json",'r') as f:
            cnt_dict = json.load(f)
        if word in cnt_dict:
            cnt_dict[word] = cnt_dict[word]+1
            sl.info(f"这个单词目前查询了{cnt_dict[word]}次")
        else:
            cnt_dict[word] = 1
            sl.info(f"这个单词目前查询了{cnt_dict[word]}次")
        with open("cnt_json.json",'w') as f:
            json.dump(cnt_dict,f)
    
        if word == "snow":
            sl.snow()
            sl.success("触发彩蛋：下雪！",icon="🌨")
        elif word == "balloons":
            sl.balloons()
            sl.success("触发彩蛋：气球！",icon='🎈')
        elif word == "豆豆":
            sl.success("触发彩蛋：小豆最厉害！hahaha",icon='😊')
        elif word == "China":
            sl.success("统一祖国 振兴中华")
            sl.image("guoqi.jpg")
    sl.image('振兴中华.jpg')
        
def home_img():
    sl.title(":sunglasses:图片处理工具:sunglasses:")
    sl.image('振兴中华.jpg')
    uploading_file = sl.file_uploader("上传图片",type=["png","jpg","jpeg"])
    if uploading_file:
        img = Image.open(uploading_file)
        sl.image(img)
        tab1,tab2,tab3,tab4,tab5,tab6 = sl.tabs(["原图","改图rbg","改图gbr","改图grb","反色","黑白"])
        with tab1:
            sl.image(img_change(img))
        with tab2:
            sl.image(img_change(img,0,2,1))
        with tab3:
            sl.image(img_change(img,1,2,0))
        with tab4:
            sl.image(img_change(img,1,0,2))
        with tab5:
            img_gray = img.convert("L")
            w,h = img_gray.size
            img_array = img_gray.load()
            for x in range(w):
                for y in range(h):
                    pix = img_array[x,y]
                    img_array[x,y] = (255-pix)
            sl.image(img_gray)
        with tab6:
            img_gray = img.convert("L")
            w,h = img_gray.size
            img_array = img_gray.load()
            for x in range(w):
                for y in range(h):
                    pix = img_array[x,y]
                    if pix < 128:
                        img_array[x,y] = 0
                    elif pix >= 128:
                        img_array[x,y] = 255
            sl.image(img_gray)

def home_liuyan():
    sl.title("留言板")
    with open("lyb_json.json",'r') as f:
        mes_list = json.load(f)
    mes_str = ''
    for i in mes_list:
        mes_str += i[0] + "：" + i[1] + "[" +i[2] + "]\n\n"
    sl.code(mes_str,language="python")
    sl.info(f"用户名：{username}")
    inm = sl.text_input("I'm")
    nm = sl.selectbox("I'm：",[username,inm,"Keeper Chen","匿名用户"])
    new_mes = sl.text_input("想要说的话……")
    but = sl.button("发送✈️")
    sl.link_button("跳转编程猫社区","https://shequ.codemao.cn/")
    if nm and new_mes and but:
        time = str(datetime.datetime.now())
        mes_list.append([nm,new_mes,time[:-10]])
        with open("lyb_json.json",'w') as f:
            json.dump(mes_list,f)
        sl.success("发送成功！刷新网页以查看最新留言板")
    sl.image("振兴中华.jpg")

def wenjuan_new(cnt):
    choose = ['A','B','C','D']
    returns = []
    returns.append("")
    returns.append({})
    title = sl.text_input(f"{cnt}.题目标题")
    while(1):
        returns[0] = title
        new = sl.button("新增选项")
        if new:
            text = sl.text_input("选项内容")
            while(1):
                enter = sl.button("确认")
                if text and enter:
                    chooses = choose[0]
                    choose.pop(0)
                    returns[1][chooses] = text
                    break
        finish = sl.button("确认题目")
        if finish:
            return returns

def home_wenjuan():
    sl.title("问卷设计(试运行)")
    cs1,cs2 = sl.columns([3,1])
    sl.info("第一个框输入标题，第二个框输入副标题")
    with cs1:
        cin1 = sl.text_input("标题")
    with cs2:
        cin2 = sl.text_input("副标题")
    if cin1 and cin2:
        sl.title(cin1)
        sl.success(cin2)
        with open("问卷星_我的网络根据地1\information.json","r") as f:
            temp4 = json.load(f)
        temp4[0] = cin1
        temp4[1] = cin2
        with open("问卷星_我的网络根据地1\information.json",'w') as f:
            json.dump(temp4,f)
        new = sl.button("新增选择题")
        with open("问卷星_我的网络根据地1\cnt_timu.json",'r') as f:
            cnt = json.load(f)
        sl.info("输入格式：题目标题/选项1#内容,选项2#内容···")
        text = sl.text_input("请输入")
        ok = sl.button("确认")
        if ("/" in text) and ("#" in text) and ("," in text) and ok:
            title = text.split("/")[0]
            temp1 = text.split("/")[1]
            temp2 = temp1.split(",")
            sl.info(temp2)
            lists = []
            lists.append(title)
            temp2_2 = []
            temp3 = {}
            for i in temp2:
                a = i.split("#")[0]
                b = i.split("#")[1]
                temp3[a] = b
            with open("问卷星_我的网络根据地1\information.json","r") as f:
                temp4 = json.load(f)
            temp2_2.append(cnt)
            temp2_2.append(temp3)
            lists.append(temp2_2)
            temp4[2].append(lists)
            with open("问卷星_我的网络根据地1\information.json",'w') as f:
                json.dump(temp4,f)
            with open("问卷星_我的网络根据地1\cnt_timu.json",'w') as f:
                json.dump(cnt+1,f)
    finish = sl.button("完成设计")
    if finish:
        with open("cnt_timu.json",'w') as f:
            json.dump(1,f)
        os.system("问卷设计.py")
    
if(page=="问卷设计(试运行)"):
    home_wenjuan()
elif(page=="问卷数据下载(试运行)"):
    pass
elif(page=="问卷数据API接口使用说明"):
    pass
elif(page=="兴趣推荐"):
    home_hobby()
elif(page=="图片处理工具"):
    home_img()
elif(page=="智慧词典"):
    home_fanyi()
elif(page=="留言板"):
    home_liuyan()
elif(page=="退出网页"):
    exit()