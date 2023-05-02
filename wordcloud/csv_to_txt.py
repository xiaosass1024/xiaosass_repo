import pandas as pd

df = pd.read_csv('/Users/xiaosass/Desktop/爬虫接单/携程评论爬取/review_detail_all.csv', header=None)
# print(df[6])
youwant = eval('6')
print(youwant)
print(len(df[youwant]))
txt = open('/Users/xiaosass/Desktop/爬虫接单/携程评论爬取/wordcloud.txt', mode='w')
for i in range(len(df[youwant])):
    txt.write(df[youwant][i]+',')
    print(df[youwant][i])