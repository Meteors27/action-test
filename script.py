import os
import requests
import spider
# import argparse

if __name__ == '__main__':
    try:
        msgList = spider.spider()
        print(msgList)
        user = os.environ['user']
        college = "竺可桢学院"
        icon = "https://raw.github.com/Meteors27/action-test/icon/ckcLogo.png"
        for msg in msgList:
            url = f"https://api.day.app/{user}/{college}/{msg['title']}?url={msg['href']}?icon={icon}"
            requests.get(url=url)
    except Exception as e:
        print(e)