import json
import os
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
registerFont(TTFont("simhei","simhei1.ttf"))
with open("information.json","r") as f:
    wenjuan = json.load(f)
title1 = wenjuan[0]
title2 = wenjuan[1]
timu = wenjuan[2]
c = canvas.Canvas(f"问卷星_我的网络根据地问卷_{title1}.pdf")
c.setTitle(f"问卷星_我的网络根据地问卷_{title1}")
c.setAuthor("Questionnaire Star-My Network Base")
c.setFont("simhei",20)
c.drawCentredString(292,790,title1)
c.setFont("simhei",17)
c.drawCentredString(350,765,title2)
y = 730
c.setFont("simhei",15)
for i in timu:
    if y<=110:
        c.drawString(50,30,"Make With Questionnaire Star-My Network Base")
        c.showPage()
        c.setFont("simhei",15)
        y = 800
    title = i[0]
    choose = i[1]
    c_no = choose[0]
    print(choose)
    chooseu = choose[1]
    KEY = list(chooseu.keys())
    c.drawString(50,y,str(c_no)+"."+title)
    y-=15

    VALUE = list(chooseu.values())
    
    for j in range(len(KEY)):
        if VALUE[j]:
            temp = "[ "+KEY[j]+" ]."+VALUE[j]+""
        else:
            temp = KEY[j]+VALUE[j]
        c.drawString(50,y,temp)
        y-=15
    y-=15
c.drawString(50,30,"Make With Questionnaire Star-My Network Base")
c.showPage()
c.save()
webbrowser.open("file://"+os.path.realpath(f"问卷星_我的网络根据地问卷_{title1}.pdf"))
        
    
    
