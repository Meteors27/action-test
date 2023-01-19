import os
import requests as re
import argparse

if __name__ == '__main__':
    try:
        user = os.environ['user']
        title = "竺可桢学院"
        content = "关于2022-2023年竺可桢奖学金评选结果的通知"
        link = "https://www.baidu.com"
        url = f"https://api.day.app/{user}/{title}/{content}/?url={link}"
        res = re.get(url=url)
        print(res.status_code)
    except Exception as e:
        print(e)