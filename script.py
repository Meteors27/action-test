import sys
import requests as re
barkCode = sys.argv[1]
url = "https://api.day.app/" + barkCode + "/Hello"
res = re.get(url=url)
print(res.status_code)