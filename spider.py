import requests
from bs4 import BeautifulSoup
# 竺可桢学院
ckcurl = ["http://office.ckc.zju.edu.cn/35005/list.htm", # 最新通知
       "http://office.ckc.zju.edu.cn/35006/list.htm", # 教学事务
       "http://office.ckc.zju.edu.cn/35007/list.htm", # 学生事务
       "http://office.ckc.zju.edu.cn/35008/list.htm", # 学生活动
       "http://office.ckc.zju.edu.cn/35009/list.htm", # 对外交流
       "http://office.ckc.zju.edu.cn/35011/list.htm", # 团委工作
    ]


def spider():
    try:
        res = []
        for url in ckcurl:
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            page = BeautifulSoup(resp.text, 'lxml')
            table = page.find('ul', class_='news_list list2')
            news = table.findAll('li')
            date = '2023-01-06'
            for record in news:
                if date in record.text:
                    title = record.findNext('a').get('title')
                    href = record.findNext('a').get('href')
                    item = {'title': title, 'href': href}
                    res.append(item)
                    # print(record.text[1:-1])
        return res
    except Exception as e:
        return e
