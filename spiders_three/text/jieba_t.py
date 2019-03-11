import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

set_list = jieba.cut("我来到了武汉华中科技大学,你知道吗",cut_all=False)

# print("Full Mode:"+",".join(set_list))

cloud_text=",".join(set_list)
print(cloud_text)
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=200, #显示最大词数
    font_path="C:\Windows\Fonts\simfang.ttf",  #使用字体
    min_font_size=15,
    max_font_size=50,
    width=400  #图幅宽度
    )
wc.generate(cloud_text)
pics = wc.to_file("pic.png")

plt.imshow(pics)
plt.axis("off")
plt.show()

