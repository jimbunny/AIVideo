# -*- coding: UTF-8 -*-
import base64
import sys,requests,json,os,re

#保存图片
def save_img(content,path,name):
                isExists=os.path.exists(path)
                if not isExists:
                        os.makedirs(path)
                i_path = path+'\\'+name
                with open(i_path,'ab') as f:
                        f.write(content)

                                #获取接口的json数据
def sougou_face(keyword,page):
    #搜狗的base64 加密，得到字符串需要转化 ，接口才可以使用
    serach_word = str(base64.b64encode(keyword.encode('utf-8')),'utf-8')
    serach_word = serach_word.swapcase()     # 实现 大写转化小写，小写转化大写
    url_send = 'http://config.pinyin.sogou.com/picface/interface/query_zb.php'
    params = 'tp=0&page='+str(page)+'&h=D9BB9D40B88283286D79B44EB3849EBE&v=8.9.0.2180&r=0000_sogoupinyin_8.9c&pv=6.1.7601&sdk=1.1.0.1819';
    url_send = url_send+'?cands='+serach_word+'&'+params
    head={"Content-Type":"application/json;charset=utf-8"}
    response = requests.get(url_send,headers=head)
    return response.content

    #解析图片
#http://i03picsos.sogoucdn.com/3057c3f30647ee17  可能存在这种图片
def list_img(sogou_data):
    json_data = json.loads(sogou_data)
    if(json_data['imglist']):
        for k in json_data['imglist']:
            img_id = k['id']   #图片唯一标识
            img_type = k['url'][-3:]
            img_list = ['jpg','gif','png']
            #不带后缀时候  可以直接赋值后缀
            if img_type not in img_list:
                img_type = 'jpg'
            response = requests.get(k['url']).content
            path = './'+k['keywords']
            save_img(response,path,img_id+'.'+img_type)
    else:
            print(u'未找到图片，停止程序')
            exit()

sogou_data = sougou_face('司机',1)
list_img(sogou_data)
exit()

#====================== 代码解释 =====================

# 1.sogou_data = sougou_face('哈士奇',1)
# 搜索关键词为哈士奇，即接口参数中的 cands，1 代表搜索第一页，其中函数返回的是二进制
# 2.list_img(sogou_data)
# 根据二进制生成对应的图片 ，在函数 list_img 里面
#          img_id = k['id']   #图片唯一标识
#             img_type = k['url'][-3:]
#             img_list = ['jpg','gif','png']
#             #不带后缀时候  可以直接赋值后缀
#             if img_type not in img_list:
#                 img_type = 'jpg'
#  就是上面所说的，返回如果没有图片后缀的话，我们自动给图片后缀为jpg，保存路径可自动更改
#  3.如果爬虫的同学，可以修改代码里面的 sougou_face('哈士奇',1)  ，即修改参数页数，sougou_face('哈士奇',2)
#  sougou_face('哈士奇',3)   sougou_face('哈士奇',4)  ，循环即可自动抓去 ，本文只显示手动抓取某一页
#  4.这是早上突发奇想完成的，代码肯定有需要改善的地方，希望各位提出，谢谢！！
#  5.最后如果你在 本地调试 ，cmd命令里面直接传参数
#  cmd   python test.py 哈士奇 1
#  只需要添加  ，至于为什么要编码 ，就是cmd窗口默认是gbk编码，我们接受的值需要转化
#  s_name = sys.argv[1].decode('gbk').encode('utf8')
# s_page = sys.argv[2]
# sogou_data = sougou_face(s_name,s_page)
# list_img(sogou_data)
# exit()