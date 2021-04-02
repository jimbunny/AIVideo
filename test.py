import requests
import json
import wave
# r = requests.options("https://nmtp.youdao.com/api/admin/nostoken?suffix=.wav&isPrivate=false")
# print(r.status_code)
# 核心请求第一步
# cookies= {"SESSION": "e99cd75c-1c56-481e-8ea4-97a2b729cdae"}
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "Connection": "keep-alive",
    "Host": "nmtp.youdao.com",
    "Origin": "https://jianwai.youdao.com",
    "Referer": "https://jianwai.youdao.com/",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "x-from": "pc"
}
# r = requests.get("https://nmtp.youdao.com/api/admin/nostoken?suffix=.wav&isPrivate=false",cookies=cookies, headers=headers)
# print(r.status_code)
# result = json.loads(r.content)["success"]
# if not result:
#     print("Session过期请重新登录！")
data = {'success': True, 'message': None, 'relatedObject': {'bucket': 'nmtp-private', 'objectname': 'COMMON_VIDEO_2021040117200636a4c71138fd4f61a08130d7f3a957f3.wav', 'token': 'UPLOAD c1465d46a9084fbcb31d8617e452832d:jXN3ZSCwd+atRgux/GytcY1bnvhhUrqq+ayM6QHWRIA=:eyJCdWNrZXQiOiJubXRwLXByaXZhdGUiLCJPYmplY3QiOiJDT01NT05fVklERU9fMjAyMTA0MDExNzIwMDYzNmE0YzcxMTM4ZmQ0ZjYxYTA4MTMwZDdmM2E5NTdmMy53YXYiLCJFeHBpcmVzIjoxNjE3MjcyNDA2LCJyZWdpb24iOiJKRCJ9'}}

# r = requests.options("https://nosup-jd1.127.net/nmtp-private/COMMON_VIDEO_20210401161727cfb77a51eb9c444ca423d7c2bed1ec9b.wav?offset=0&complete=false&context=&version=1.0")
# print(r.status_code)

headers = {
  "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
  "Accept" : "*/*",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
  "Connection" : "keep-alive",
  "Content-Length": 4194304,
  "Host": "nosup-jd1.127.net",
  "Origin": "https://jianwai.youdao.com",
  "Referer": "https://jianwai.youdao.com/",
  "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
  "sec-ch-ua-mobile": "?0",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "cross-site",
  "x-nos-token": data.get("relatedObject").get("token")
}
parms = ""
# r = requests.post("https://nosup-jd1.127.net/nmtp-private/" + data.relatedObject.objectname + "?offset=0&complete=false&context=&version=1.0", headers=headers, data =parms)
# print(r.status_code)
f = open(r"test.txt","rb").read()
print(f)