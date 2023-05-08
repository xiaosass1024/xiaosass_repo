import nltk
from nltk.collections import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# f = open('/Users/xiaosass/Desktop/爬虫接单/英语idiom词频统计/sample1.txt')
# sample = f.read()
# print(sample)


finder = nltk.collocations.BigramCollocationFinder.from_words(nltk.corpus.genesis.words('sample1.txt'))
finder.apply_freq_filter(3)
finder.nbest(bigram_measures.pmi, 10)
print(finder.nbest(bigram_measures.pmi, 100))