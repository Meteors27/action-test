import argparse
import os
import requests as re
# parser = argparse.ArgumentParser(description='Get Bark ID')
# parser.add_argument('--user', '-u', help='Bark ID', required=True)
# args = parser.parse_args()

if __name__ == '__main__':
    # try:
    #     print("args.user = "+args.user)
    #     url = "https://api.day.app/" + args.user + "/Hello"
    #     res = re.get(url=url)
    #     print(res.status_code)
    # except Exception as e:
    #     print(e)
    user = os.environ['user']
    url = "https://api.day.app/" + user + "/Hello"
    res = re.get(url=url)
    print(res.status_code)