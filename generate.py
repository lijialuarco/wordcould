from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)
# 爬取文本
r = requests.get("https://en.wikipedia.org/wiki/Artificial_intelligence")
soup = BeautifulSoup(r.text, 'html.parser')
f = open('data.txt', 'w')
f.write(soup.get_text())
f.close()
# 读文本文件
text = open(path.join(d, 'data.txt')).read()

# 读取自定义图片
alice_coloring = np.array(Image.open(path.join(d, "dog.jpg")))

# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white", max_words=2000,
               mask=alice_coloring, max_font_size=60, random_state=102, scale=8,
               font_path="book.otf").generate(text)

wc.generate_from_text(text)
print('开始加载文本')
# 改变字体颜色
img_colors = ImageColorGenerator(alice_coloring)
# 字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc, interpolation="bilinear")
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
# 获得模块所在的路径的
d = path.dirname(__file__)
# 将多个路径组合后返回
wc.to_file(path.join(d, "h16.jpg"))
print('生成词云成功!')
