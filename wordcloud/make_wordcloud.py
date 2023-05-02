import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('/Users/xiaosass/Desktop/爬虫接单/携程评论爬取/wordcloud.txt') as f:
    data = f.read()

'''文本预处理，去除一些无用的字符，只取出中文'''
new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
new_data = " ".join(new_data)

'''文本分词'''
seg_list_exact = jieba.cut(new_data, cut_all=True)
object_list = []

'''加载停用词'''
with open('/Users/xiaosass/Desktop/xiaosass_repo/wordcloud/baidu_stopwords.txt', encoding='utf-8') as f:
    con = f.readlines()
    stop_words = set()
    for i in con:
        stop_words.add(i.strip())

'''去除停用词及单个词'''
for word in seg_list_exact:
    if word not in stop_words and len(word) > 1:
        object_list.append(word)
# print(object_list)

'''词频统计'''
word_counts = collections.Counter(object_list)
word_counts_top100 = word_counts.most_common(100)
# print(word_counts_top100)

'''绘制词云'''
my_cloud = WordCloud(
    background_color='white',
    width=900, height=900,
    max_words=50,
    font_path='/Users/xiaosass/opt/anaconda3/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf',
    max_font_size=99,
    min_font_size=16,
    random_state=50
).generate_from_frequencies(word_counts)

'''生成词云图'''
plt.imshow(my_cloud, interpolation='bilinear')
'''无坐标轴设置'''
plt.axis('off')
plt.show()