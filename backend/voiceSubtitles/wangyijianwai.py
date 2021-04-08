import requests
import json
url = "https://nmtp.youdao.com/api/organize/161498/video"
data = {
    "audio": 1,
    "captionType": 2,
    "lan": "zh",
    "recogFlag": 0,
    "sourceUrl": "https://nmtp-private.nos-hz.163yun.com/COMMON_VIDEO_20210406165319738f13db3bfc4616b465083cb380ce3f.wav",
    "title": "test2",
    "trans": 0
}
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br"
    "Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": 195,
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1590565496.6677682; _ga=GA1.2.1039362489.1617013280; UM_distinctid=17890ae3b5ed5c-026d19a77fb765-c3f3568-1fa400-17890ae3b5f8a2; _gid=GA1.2.1079486879.1617698926; SESSION=0cbdc007-8636-4706-b0c3-01846a5bef3e; NTES_SESS=Z7j_D6QQmrYhg77nDy0Y4LKIZMZkmH2bdz.zM1Oy4lmc8Ftg8d_0OTsMRCtVBEUHJD27RimWmjk6hDsHRY6svtE62NfysnKS5PS4OnDVbg0PeMUQXikxAWJCjAMpXxGlHyqK3Q6nr.rcbugImf9icV5oMU5OzsKNbvUgE_pu.OjL54t1Biy92mTdK5TysCbNBrdMV5f0wCjyQYejGCkLyigDI; S_INFO=1617698929|0|#3&80#|jingtongyu@126.com; P_INFO=jingtongyu@126.com|1617698929|0|youdao_jianwai|00&99|TH&1617619067&mail_client#TH&null#10#0#0|&0|godlike_app&mail126&youdao_jianwai|jingtongyu@126.com",
    "Host": "nmtp.youdao.com",
    "Origin": "https://jianwai.youdao.com",
    "Referer": "https://jianwai.youdao.com/",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "x-from": "pc"
}
r = requests.post(url=url, data=data)
print(r.status_code)
print(r.status_code)

url = "https://nmtp.youdao.com/api/organize/161498/articles/status?articleIds=18522072"