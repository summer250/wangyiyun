# Matplotlib是一个 Python 的 2D数学绘图库
# 安装：pip install matplotlib
import matplotlib.pyplot as plt
# jieba中文分词库
# 安装：pip install jieba
import jieba
# wordcloud词云库
# 安装pip install wordcloud
from wordcloud import WordCloud
from cv2 import *

# 1.读入txt文本数据
text = open(r'/Users/daoshilaoba/Desktop/test.txt', "r",encoding='gbk').read()
#print(text)
# 2.结巴中文分词，生成字符串，默认精确模式，如果不通过分词，无法直接生成正确的中文词云
cut_text = jieba.cut(text)
# print(type(cut_text))
# print(next(cut_text))
# print(next(cut_text))
# print(next(cut_text))
# 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
result = " ".join(cut_text)
# print(result)
# 3.生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
image_path = "/Users/daoshilaoba/Desktop/timg (1).jpg"
img = cv2.imread(image_path)
wc = WordCloud(
        font_path=r'/System/Library/Fonts/Hiragino Sans GB.ttc',
        background_color='white',
        mask=img,
        )
# 产生词云
wc.generate(result)
# 保存图片
wc.to_file(r"/Users/daoshilaoba/Desktop/wordcloud.png")  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
# 4.显示图片
# # 指定所绘图名称
plt.figure("jay")
# 以图片的形式显示词云
plt.imshow(wc)
# 关闭图像坐标系
plt.axis("off")
plt.show()
