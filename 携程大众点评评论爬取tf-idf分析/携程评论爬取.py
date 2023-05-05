import requests
import csv
import time
import random

url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList'
headers = {
    'cookie': 'GUID=09031072317742948532; _RSG=gpqDKvgylOCrzu_It7hQy9; _RDG=28a96f477ba0f226cf0f664ccacb184152; _RGUID=c62ff2ae-5437-4cea-9f1a-ac7dd2ff8f75; _bfaStatusPVSend=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; MKT_CKID=1679894715670.vvwl8.d4ej; login_uid=B290BAE5C92FFE4CB5C459A90B10D439; login_type=0; cticket=FE346E47377E6D86C45C6DDCB41D7D66898BC9AA3A3C0A2659C4BFE7A1C39D77; AHeadUserInfo=VipGrade=5&VipGradeName=%B0%D7%D2%F8%B9%F3%B1%F6&UserName=&NoReadMessageCount=0; DUID=u=B290BAE5C92FFE4CB5C459A90B10D439&v=0; IsNonUser=F; UUID=E257759509EA4646984E73F060443DFA; Session=SmartLinkCode=ctrip&SmartLinkKeyWord=&SmartLinkQuary=_UTF.&SmartLinkHost=ctrip.com&SmartLinkLanguage=zh; intl_ht1=h4=477_5998495,477_35501475,477_828374,477_1483622,477_71976881,477_106382373; _RF1=122.238.53.211; MKT_Pagesource=PC; nfes_isSupportWebP=1; MKT_CKID_LMT=1683287405147; _bfa=1.1679894667914.1tl0hxd.1.1681895916585.1683287399628.6.39.212094; _bfs=1.3; _ubtstatus=%7B%22vid%22%3A%221679894667914.1tl0hxd%22%2C%22sid%22%3A6%2C%22pvid%22%3A39%2C%22pid%22%3A0%7D; _bfi=p1%3D290510%26p2%3D0%26v1%3D39%26v2%3D38; _bfaStatus=success; _jzqco=%7C%7C%7C%7C1683287405469%7C1.1787196504.1679894715579.1683287405150.1683287417874.1683287405150.1683287417874.undefined.0.0.31.31; __zpspc=9.5.1683287405.1683287417.2%234%7C%7C%7C%7C%7C%23',
    'cookieorigin': 'https://you.ctrip.com',
    'origin': 'https://you.ctrip.com',
    'pragma': 'no-cache',
    'referer': 'https://you.ctrip.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}


# 请求函数
def req_url(json_var):
    time.sleep(1 + random.random())
    res = requests.post(url=url, json=json_var, headers=headers)
    # print(res.json())
    return res.json()


def json():
    for page in range(1, 189):
        print(f'===========正在爬取第{page}页===========')
        yield {"arg": {"channelType": 2, "collapseType": 0, "commentTagId": 0, "pageIndex": page, "pageSize": 10,
                       "poiId": 77591, "sourceType": 1, "sortType": 3, "starType": 0},
               "head": {"cid": "09031072317742948532", "ctok": "", "cver": "1.0", "lang": "01", "sid": "8888",
                        "syscode": "09", "auth": "", "xsid": "", "extension": []}}


# 解析字典数据
def parse_dict(dict_data):
    review_list = dict_data['result']['items']
    # print(review_list)
    for review_item in review_list:
        content = review_item['content']
        print([content])
        yield [content]


# 数据持久化函数
def save_file(filename, content):
    with open(filename + '.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(content)


if __name__ == '__main__':
    for json in json():
        hotel_dict_data = req_url(json)
        for info_list in parse_dict(dict_data=hotel_dict_data):
            save_file('ctrip_comment', info_list)
