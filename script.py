import os
import requests
import spider
# import argparse

if __name__ == '__main__':
    res = spider.spider()
    print(res)
    try:
        user = os.environ['user']
        title = "竺可桢学院"
        content = "关于2022-2023年竺可桢奖学金评选结果的通知"
        link = "https://www.baidu.com"
        icon = "https://raw.github.com/Meteors27/action-test/icon/ckcLogo.png"
        url = f"https://api.day.app/{user}/{title}/{content}?url={link}?icon={icon}"
        requests.get(url=url)
    except Exception as e:
        print(e)