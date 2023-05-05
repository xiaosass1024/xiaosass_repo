import requests
import parsel
import csv
import time


api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=oab695bmapnug0qzwf6c&num=1&signature=oud5nw1wgrnyf2m5830hvo18b6&pt=1&sep=1"

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
    'Cookie': '_lxsdk_cuid=1879454e6ebc8-009a6bc56d4b27-1d525634-157188-1879454e6ebc8; _hc.v=5e471d00-09ee-0b34-1916-daf0edbd32a9.1681820805; WEBDFPID=wy5669u78v225vz0z84786u769v6x930812054496x3979588wu84y56-1997180812045-1681820811330UEKIEQA75613c134b6a252faa6802015be905519217; _ga=GA1.2.961811037.1682993561; uuid=E1530091E2051D4D9D4DDAAE38A3271AAA199C7A433F3771AEA95A5C4648B327; iuuid=E1530091E2051D4D9D4DDAAE38A3271AAA199C7A433F3771AEA95A5C4648B327; _lxsdk=E1530091E2051D4D9D4DDAAE38A3271AAA199C7A433F3771AEA95A5C4648B327; pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE/ZGV2aWNlX3N5c3RlbT1NQUNJTlRPU0gmeW9kYVJlYWR5PWg1Pjo8MTY4MzI5MDA5MzgyMl1fWw=="; m_flash2=1; fspop=test; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1681820805,1683290098; s_ViewType=10; qruuid=8d26e661-cad4-457b-b84f-3e2093dda7ea; dplet=b261bde2ca805acdb98bcf1e1e863bf6; dper=d171aaaeefa9712ea4a90a057ceaa4bbc2a5b33ba8c01dd785542b7f00adea58e7e0356bd407f46789ac84099228cec96cde53c2a7b6a75a77285f51efd280d3; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%B0%8F%E8%90%A8SS; ctu=d57cadb4adcdb2b77298103d00d213a3fd44d307a3ae8c8eaa1422752a28ac2f; cy=16; cye=wuhan; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1683290373; _lxsdk_s=187ebe87937-27-ef8-196%7C%7C449',
    'Host': 'www.dianping.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dianping.com/shop/G54WVFofmyeV5iWN/review_all/p2',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}


def get_data(page):
    time.sleep(1)
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
    for page in range(47, 101):
        data = get_data(page)
        for result in parse_data(data):
            save_data('大众点评评论.csv', result)


if __name__ == '__main__':
    run()
