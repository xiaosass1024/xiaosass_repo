import requests
import time
import random

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
headers = {
    'cookie': 'lastCity=101210300; __zp_seo_uuid__=2b8f7603-848c-4a35-abcd-6d41f4c6ba4c; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1683727560; wd_guid=1ecbe228-4d82-48aa-9cfd-a05db5e22b6b; historyState=state; _bl_uid=k0lmFhdsh0grkyxXzrvCms5kOh73; __fid=309027e9b417727b87dbb175e2b4ef56; boss_login_mode=sms; gdxidpyhxdE=s69Y5VGatOaLcSJhWDSm7g20s8TJHCla%5CGDKW8fKK6%2B%2BbOU5A8zQqt5kf2xbcJXSEa29%5CeXoRmOhfLY5RO7zzDQN2mGw%2BgmskhPH%5C%2Bc7jmWXXnJph%5CVb%2Bzqed1tAqhraq9QJ%5CybtIwOaA%2B8eqPf%5Ct7e6r3eu2OSSN7YuEuhRCDk8%5CGiC%3A1683730163924; YD00951578218230%3AWM_NI=xSh1Cb5sPOjWGS6jArkbhoAi5OdgANgCY7SRnsCCNHkZeJ4WKU7e1tUC%2F6WkFgNuffPQ0bGD1c%2Fnx18BPbk4UPnmRdo0qIqW7%2FVzQWRb9BEb297SWkL2MUCvqlwztxlRdmU%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6d86ff2bea0acb654878e8bb7c84f869f8eb1c474938fbda3f9458ee99caff12af0fea7c3b92abc8da8d2c26af7ada0b0e95d858dfa8bc47aa9bea890c463f791ac88c446a59d97d8d25aaead8da4cd44a986ababb75d898bf986b480979de1d7d66186b98296e56e948f0083c650f3bde18ffb3bfc9ea083ea409790a28ed170adf0bfaaf45df5f19a9bd45d92bef7a3c86af2e7f9b4d66190ee83b6c27eb3b4b99bf774b08eac8ed837e2a3; YD00951578218230%3AWM_TID=%2BNdmz%2FZT0HJEUQQQVUfEgQFpQnbNuXZ%2F; wt2=DjgPbtQD6JKtPul-ajsk490_c1Fg31oS_HLfdLXvxZ1qatIr0gz4yzwQD1gpVDKp3NOZQBnmsUxQgvRIINf3d0g~~; wbg=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1683729776; __c=1683727560; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E6%25B1%25BD%25E8%25BD%25A6%25E7%2594%25B5%25E5%25AD%2590%26city%3D101210300&s=3&g=&friend_source=0&s=3&friend_source=0; __a=63769514.1683727560..1683727560.17.1.17.17; geek_zp_token=V1RNMgE-373VZiVtRvxx4fKiuz7z3Wwys~; __zp_stoken__=4b78ePHlSQhYWCmBFSUd4eXFMQEBTKldYdBIhJRgsGj5xDFl%2BRzZdfRkcc0pHGHkbQUdHIFVdRRgGGD4AARFzancBKgdAPxUpGh0KTyMMIhxiICICIH87O3V3ayYJaElxA351WwY8SGRRXSU%3D',
    'pragma': 'no-cache',
    'referer': 'https://www.zhipin.com/web/geek/job?query=%E6%B1%BD%E8%BD%A6%E7%94%B5%E5%AD%90&city=101020100&page=3',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}


def params(page):
    return {
        'scene': '1',
        'query': '汽车电子',
        'city': '101020100',
        'experience': '',
        'payType': '',
        'partTime': '',
        'degree': '',
        'industry': '',
        'scale': '',
        'stage': '',
        'position': '',
        'jobType': '',
        'salary': '',
        'multiBusinessDistrict': '',
        'multiSubway': '',
        'page': str(page),
        'pageSize': '30',
    }


for page in range(1, 6):
    time.sleep(random.randint(1, 3))
    response = requests.get(url=url, headers=headers, params=params(page=page))
    print(response.text)
