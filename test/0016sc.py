#coding:utf-8
import random
import string
import sys
import math
from PIL import ImageFont,ImageDraw,ImageFilter,Image
#字体路径
font_path=r"C:\Users\Tsinghua-yincheng\Desktop\SZday17\font\Georgia.ttf"
#位数
numbers=4
#验证码大小
size=(150,60)
#背景颜色
bgcolor=(255,255,255)
#字体颜色
fontcolor=(0,0,0)
#line 干扰线
draw_line=True
line_numbers=(1,5)

def  bgfontrange():
    global  bgcolor
    color1=random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    bgcolor=(color1,color2,color3)
def  ftfontrange():
    global  fontcolor
    color1=random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    fontcolor=(color1,color2,color3)

def  make_text():
    source1= [str(x) for  x in range(0,10)] #0-9之间
    source2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    source3=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    source=[]
    source.extend(source3)
    source.extend(source1)
    source.extend(source2)
    return "".join(random.sample(source,numbers)) #"",加上4个随机数
#print make_text()随机划线
def  make_line(draw,width,height):
    begin=(random.randint(0,width),random.randint(0,height))
    end = (random.randint(0,width), random.randint(0, height))
    draw.line([begin,end], fill=fontcolor,width=3)  # 绘线
#生成验证码
def make_codepng():
    width,height=size #图片的宽度与高度
    image= Image.new("RGBA",(width,height),bgcolor)#创建图片
    draw=ImageDraw.Draw(image)#绘图工具
    text=make_text() #生成随机字符串
    font=ImageFont.truetype(font_path,40)#字体
    font_width,font_height=font.getsize(text) #字体的宽度与高度
    draw.text( ((width-font_width)/numbers,(height-font_height)/2), #写入了文字
               text,
               font=font,
               fill=fontcolor) #写入文字

    if  draw_line:
        print("make_line")
        num=random.randint(1,6)
        for i in range(num):
            make_line(draw,width,height)

    image=image.transform((width+30,height+20),
                          Image.AFFINE,
                          (1,-0.5,0,-0.2,0.9,0),
                          Image.BILINEAR) #扭曲
    image=image.filter(ImageFilter.RankFilter) #处理边界
    filename=u"C:\\Users\\Tsinghua-yincheng\\Desktop\\SZday17\\code\\生成验证码\\code5"+"\\"+text+".png"
    with open(filename, "wb") as file:
        image.save(file, format="png")


for i  in range(100):
    bgfontrange()
    ftfontrange()
    make_codepng()