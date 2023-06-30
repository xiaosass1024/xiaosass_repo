import json

import scrapy

from ..items import KailiItem


class KailiSpiderSpider(scrapy.Spider):
    name = "kaili_spider"
    allowed_domains = ["cnncmall.com"]
    # start_urls = ["http://cnncmall.com/"]
    url = 'https://www.cnncmall.com/cnnc/mall/noauth/searchGoods'
    headers = {
        'Cookie': 'auth-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjU5MDUwOTkwMTg1MTIwNTY0NywiaWF0IjoxNjgyODM1NTg0MDk5LCJsb2dpblNvdXJjZSI6InBjLXdlYiJ9.T-u-o7tpMKNtndJfqI2zFNHBk07Y37UhZyiRKOEngGA',
        'Host': 'www.cnncmall.com',
        'Origin': 'https://www.cnncmall.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    def data(self, page):
        return {"queryStr": "", "queryChannelId": "1008", "categoryId": "", "catalogName": "", "level": "",
                "brandId": "",
                "supplierShopId": "", "orderByColumn": "", "orderType": 0, "queryParams": [
                {"filterId": "vendor_id_name", "filterName": "供应商", "filterValues": ["京东（员工活动）"],
                 "categoryId": ""}], "agreementId": "", "minSalesPrice": 0, "maxSalesPrice": "",
                "orgPath": "1-305775845729763327-400000010000062520-400000010000062521-400000010000062556-",
                "userId": "590509901851205647", "pageSize": 10, "pageNo": page, "activityId": "843819168674254848",
                "doContract": "false", "doActity": "true", "doSelect": 1, "commodityTypeIds": [], "havStock": 0,
                "qryToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjU5MDUwOTkwMTg1MTIwNTY0NywiaWF0IjoxNjgyNDI4NjA2NTE5LCJsb2dpblNvdXJjZSI6InBjLXdlYiJ9.KNKoB9Qp9ORGoej6qdFKWQUeKogadJUtrtTw0gZlph8",
                "rsGoodsSearch": "false", "psDiscountRate": 0, "doMallContract": "true", "memUserType": "4", "supId": 0,
                "outerUserTypes": ["4"], "province": "15", "city": "1243", "county": "1248", "town": "54971"}

    def start_requests(self):
        for page in range(1, 101):
            yield scrapy.Request(url=self.url, body=json.dumps(self.data(page)), method='POST', headers=self.headers,
                                 callback=self.parse_list)

    def parse_list(self, response):
        dict_data = response.json()
        results = dict_data['data']['result']
        for result in results:
            catalogAllName = result['catalogAllName']
            commodityName = result['commodityName']
            marketPrice = result['marketPrice']
            salePrice = result['salePrice']
            supplierName = result['supplierName']
            # print(KailiItem(catalogAllName=catalogAllName, commodityName=commodityName, marketPrice=marketPrice,
            #                 salePrice=salePrice, supplierName=supplierName))
            print(catalogAllName, commodityName, marketPrice, salePrice, supplierName)
            yield KailiItem(catalogAllName=catalogAllName, commodityName=commodityName, marketPrice=marketPrice,
                            salePrice=salePrice, supplierName=supplierName)
