# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CSVKailiPipeline:

    def open_spider(self, spider):
        self.f = open('京东.csv', mode='a', encoding='utf-8', newline='')
        self.csv_writer = csv.DictWriter(self.f,
                                         fieldnames=['品类', '品名', '市价', '折价',
                                                     '商家'])
        self.csv_writer.writeheader()

    def process_item(self, item, spider):
        d = dict(item)
        # print(d)
        self.csv_writer.writerow(
            {'品类': d['catalogAllName'], '品名': d['commodityName'], '市价': d['marketPrice'], '折价': d['salePrice'],
             '商家': d['supplierName'], })
        return item

    def close_spider(self, spider):
        self.f.close()
