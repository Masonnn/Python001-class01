'''
爬取猫眼电影top10
电影名称
类型
上映时间
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# 需要爬取的页面
url = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
cookie = '__mta=244030394.1593073122165.1593078999038.1593081633842.9; uuid_n_v=v1; uuid=7A0F4770B6BC11EAACB6BBD781D899382353DC4B16A84BF9BE532908BC8308DB; _csrf=a42231a2bcccb4006af2825c69d00166c86874f7760aa9513457c336c358b32a; _lxsdk_cuid=172ea8eb9dac8-09d95878794db4-143f6257-13c680-172ea8eb9dbc8; _lxsdk=7A0F4770B6BC11EAACB6BBD781D899382353DC4B16A84BF9BE532908BC8308DB; mojo-uuid=0d93c9cc79709f5864439721bbe5a609; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593073122,1593073140,1593075062; mojo-session-id={"id":"4635ea9063bf90b6d4cf6796f86625d5","time":1593083886753}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593083896; __mta=244030394.1593073122165.1593081633842.1593083896094.10; _lxsdk_s=172eb107cc0-68-fb9-b8f%7C%7C11'

header = {}
header['user-agent'] = user_agent
header['cookie'] = cookie
response = requests.get(url, headers=header)
print(f'返回状态码是：{response.status_code}')

bs_info = bs(response.text, 'html.parser')


# 处理字符串
def parse_text(str):
    return str.strip().split('\n')[-1].strip()


movies = []

for tagslevel1 in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    for tagslevel2 in tagslevel1.find_all('div', attrs={'class': 'movie-hover-title'}):
        for i in tagslevel2.find_all('span', attrs={'class': 'hover-tag'}):

            if i.text == '类型:':
                film_genre = parse_text(i.parent.text)
            if i.text == '上映时间:':
                play_date = parse_text(i.parent.text)
                film_name = parse_text(i.find_parent('div').get('title'))

                movie = [film_name, film_genre, play_date]
                movies.append(movie)

movie1 = pd.DataFrame(data=movies[:10], columns=['电影名字', '类型', '上映日期'])

movie1.to_csv('./movie01.csv', encoding='utf8', index=False, header=True)
