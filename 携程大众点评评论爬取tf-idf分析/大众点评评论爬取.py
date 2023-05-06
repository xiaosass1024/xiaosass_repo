import requests
import parsel
import csv
import time
import random
from fake_useragent import UserAgent

ua = UserAgent()
api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=oab695bmapnug0qzwf6c&num=1&signature=othvcohgqfxuq0odhi23bjc1jh&pt=1&sep=1"

# 获取API接口返回的代理IP
proxy_ip = requests.get(api_url).text

# 用户名密码认证(私密代理/独享代理)
username = "d2284304147"
password = "xkwffs8m"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
}
print(proxies)


def url(page):
    if page == 1:
        return 'https://www.dianping.com/shop/G54WVFofmyeV5iWN/review_all'
    else:
        return 'https://www.dianping.com/shop/G54WVFofmyeV5iWN/review_all/p' + str(page)


headers = {
    'Cookie': '_lxsdk_s=187f0c00c20-f0-a4a-9d6%7C%7C266; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1683371349; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1683369140; s_ViewType=10; cy=16; cye=wuhan; ll=7fd06e815b796be3df069dec7836c3df; dper=78b640b3cdb345a1f7cbfcae5cb47936cb9c7d681cc797694438e2d8cadec0a17c65acf325cd625a40cef8752ae5e74a4d40da752fe5fda920de1a326d7acfec; qruuid=04fee826-fedd-433e-9baf-84e5a41c5597; WEBDFPID=yu83xuz28y675568ywv3x17vwz19zuy7812u90u57xw9795881uuy196-1998729181973-1683369180866GKYQMQW8916c935af78ba3b6588b79f938ed96b1512; _hc.v=0dc66f04-fb9e-2a7b-0405-da3e64338c90.1683369140; _lxsdk=187f09ea04cc8-03a7b41dc3f6398-3a626b4b-157188-187f09ea04cc8; _lxsdk_cuid=187f09ea04cc8-03a7b41dc3f6398-3a626b4b-157188-187f09ea04cc8; fspop=test',
    'Host': 'www.dianping.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dianping.com/shop/G54WVFofmyeV5iWN/review_all/p1',
    'User-Agent': ua.opera
}


def get_data(page):
    time.sleep(random.randint(5, 8))
    response = requests.get(url(page), headers=headers, proxies=proxies)
    print(response.status_code)
    # print(response.text)
    print(f'==================正在爬取第{page}页==================')
    return response.text


def parse_data(data):
    selector = parsel.Selector(data)
    selector_list = selector.css('.reviews-items > ul > li')
    for li in selector_list:
        comment = li.css('.main-review > .review-words::text').get().strip().replace('\n', '')
        print(comment)
        yield [comment]


def save_data(filename, content):
    with open(filename, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(content)


def run():
    ua.update()
    for page in range(161, 170):
        data = get_data(page)
        for result in parse_data(data):
            save_data('大众点评评论61_.csv', result)


if __name__ == '__main__':
    run()
