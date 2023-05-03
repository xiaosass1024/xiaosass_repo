import time

import requests

url = 'https://minsu.dianping.com/api/phx/cprod/products'
headers = {
    'Cookie': '_lxsdk_cuid=1879454e6ebc8-009a6bc56d4b27-1d525634-157188-1879454e6ebc8; _hc.v=5e471d00-09ee-0b34-1916-daf0edbd32a9.1681820805; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1681820805; WEBDFPID=wy5669u78v225vz0z84786u769v6x930812054496x3979588wu84y56-1997180812045-1681820811330UEKIEQA75613c134b6a252faa6802015be905519217; dper=f634da77fefa5619d36712c118e2844c3cebeb6e25756412bdb9b02941946a8ad79c1b4be76ffc09b7be3623cac96ea96fcc58109781e535f6cf25607810b23e; cy=288; cye=ali; phx_wake_up_type=mtpc_category; _ga=GA1.2.961811037.1682993561; _gid=GA1.2.1293429019.1682993561; zgwww=66045240-e88f-11ed-a086-3916501f9ab5; phx_wake_up_source=nav; zg.userid.untrusted=24742532; token2=AgGpIUr8La4zJjoUOkcAIudTAw75_Jf7NjRy9LrKRgDP_9y59D3JXSCRilpXEd8S3ctgHFSIw-B6DQAAAAAtGAAA6q6dlu0orEKd4DrYJR-h3tK7_uF7X7g7VwQryrdGshnbmrd5BYEBLoQlPkp1ZHrW; userid=1710; uuid=E1530091E2051D4D9D4DDAAE38A3271AAA199C7A433F3771AEA95A5C4648B327; iuuid=E1530091E2051D4D9D4DDAAE38A3271AAA199C7A433F3771AEA95A5C4648B327; _lxsdk=E1530091E2051D4D9D4DDAAE38A3271AAA199C7A433F3771AEA95A5C4648B327; bottom-cover-closed=true; XSRF-TOKEN=7RveYcVt-f-P_E9VO2j0YlBFl43mm1SSefNA; _lxsdk_s=187db0b5d3e-31a-1f6-ed8%7C%7C85',
    'Host': 'minsu.dianping.com',
    'Referer': 'https://minsu.dianping.com/ningbo/d330203/pn3/?dateBegin=20230502&dateEnd=20230503',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}


def params(page):
    return {
        'dateBegin': '20230502',
        'dateEnd': '20230503',
        'cityPinyin': 'ningbo',
        'locationCategory': 'd',
        'locationId': '330203',
        'pageNow': str(page),
        'isInternal': 'false',
        '_token': 'eJx9lgty7SgMRLcE+iB7OTbY+1/CHMm+9yUzUy9VSSELaH26RYYNHzJ0NH6PsY//sTX+7n/tjr3+4v/YTfYxvzaeaNhb9LHHUtNTQ51vfNdLmx46+DpUdOHpqlgSB38P7KY9NtaB96pdps668XvrLXdsMqLOcPMuU0U4K4bv0ju6dM5hyy5XnP85f0kfEZ1vjh3f+FwCtKviUVZvfG4WpHvLITEu8hG58XfPzDbdyKpTkFDxTZqsyg1snX556CWXbyB1sMjcJbF8x08E0jTPXbJx3sue+PqY1M5sko/LkklVZ0h43OpjUGUfJ/UdwV7JypdFzaW+RliMJ/+RZqeLqpMMNPZxRn6xuOWsDt8yZfg2Nuybu5brz3zNhCDG9EUA005yvIWmD6Us9HcEfrPO3mQVrQkbnT9N3I+MFjTie+Kx6WJhIj5uGNHlzvhkyO7JmT225A43HWK2kefkBu5jP3WWaYcbMffgg3U7iKXxhY4ST9DbZN8g390W92z4xdUadBLJ+zrtuSo/e/o1uvtjS1T/Qk+ygD/sTX6c2J2eNrq+YcMSbPKmY8eYcBZmE6OwI6vr/HRq5899pSBYQv3DTrQyRcnDgMh+TTnpIf2nUeQ4Dt2km9sJqwIuLDkIzKBht912uVMYVHinCq16Qc7sdujKHl1Ck1MP9OK0M2VmT373E480gIS1gcpZ1WQV/CM+XdCRLDz3Zv+7k72qZN7JXBiU+tFWOm3cuiQVQ9mVKVCqHqkg1tdbT8MmBZQFNoqiZ/PQyR4QqCjKfCogqf4DnTAfXsTBmQ8iFK7TD2JiaiGm4ugJ6/h2MMmZk0UK8SzFjhcPtf/AQ6cZ9YvXqMQHL39Svx88ZAFGxjdYF/aLN3JuSdTpxHPwUjQP3s7qD95VeJ+KMsW+ePLMvBcvMazwrpooi7W8eEoOvfCs8LTw+otHND/wlmaNvPA0J96L14vJDbY9eJ6zD4wTvHix+xfv08EnvwBv1Tx5+hW/8LLWgnfPSV71rInxzmGrCE95lDS576p4mE/VYZfn/k+N02pEtWoul8Ir3uzZU8+R1fgVb6v5HcVG8Ktz4D0TqOa6wrk//RqF9/DRi4OWE4n79vI+b0K+MBP/xm2ffDOj7fW3qlu+WfHLf7x+ef2Hnr/8819+eCs9X4iPXzfPF+9iIvGWyPLkc2S8TFK076ltpmTlO/GXzfyQfNHcXv/XJue8Vb72ZVmfrOcofr78IaMJe8bzWqe+iLEmRvGTEcY0z4mQ92XNbyKv/tR99t63vvclA4+sbul6r4qhb1u2cr+ZN9/8fWFK8VntnLDoxYo9r74+9ZNSf+ohtZkVPEVrfhAv7/aebKO+qc9dchJd7Mj/QeBEDmqwu/B/iScf4DiTm/N++or1DyCkIjI='
    }


def get_info(page):
    for i in range(1, page + 1):
        res = requests.get(url, headers=headers, params=params(i))
        dict_data = res.json()
        time.sleep(1)
        room_list = dict_data['data']['list']
        for room in room_list:
            print(room['title'], room['usableArea'], room['avgFinalPrice'])


if __name__ == '__main__':
    get_info(10)
