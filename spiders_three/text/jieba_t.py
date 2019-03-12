import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# C:\Users\Administrator\Desktop\sp

filename = input("输入文件名:")
text = open("{}.txt".format(filename)).read()
set_list = jieba.cut(text,cut_all=False)
# print("Full Mode:"+",".join(set_list))
cloud_text=",".join(set_list)
print(cloud_text)

#词云配置
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=200, #显示最大词数
    font_path="C:\Windows\Fonts\simfang.ttf",  #使用字体,此为windows默认路径
    min_font_size=15,
    max_font_size=50,
    width=800 , #图幅宽度
    height = 800
    )
wc.generate(cloud_text)
#保存图片
pics = wc.to_file("pic.png")

plt.imshow(pics)
plt.axis("off")
plt.show()

