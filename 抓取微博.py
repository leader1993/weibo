#!/usr/bin/env python
#conding:utf8
import requests
import pandas as pd
import csv
import time


'''
https://m.weibo.cn/api/container/getIndex?containerid=2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO
containerid: 2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO
https://m.weibo.cn/api/container/getIndex?containerid=2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=2
containerid: 2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO
page_type: 03
page: 2

containerid: 2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO
page_type: 03
page: 3
'card_type': 31, 'itemid': '', 'scheme': 'https://m.weibo.cn/search?profile_containerid=231802_7371737498&profile_uid=6007443584&disable_sug=1&diabled_eject_animation=1&disable_hot=0&trans_bg=0&disable_history=1&hint=%E6%90%9C%E4%BB%96%E7%9A%84%E5%BE%AE%E5%8D%9A&luicode=10000011&lfid=2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO&container_ext=profile_uid%3A6007443584%7Chint%3D%E6%90%9C%E4%BB%96%E7%9A%84%E5%BE%AE%E5%8D%9A%7Cnettype%3A%7Cgps_timestamp%3A1590850354&containerid=100103type%3D401%26t%3D10%26q%3D', 'desc': '搜他的微博'}
Traceback (most recent call last):
'''

url = 'https://m.weibo.cn/api/container/getIndex'
header = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'cookie': 'SUB=_2A25z1XSiDeRhGeFN7FMW8ynIwjSIHXVRNhzqrDV6PUJbkdANLUvBkW1NQ_fggYqXGip7oCMNvXyRJGY91Lv3dbm7; SUHB=0C1C5xe3Z5S0Gw; _T_WM=44705814025; MLOGIN=1; WEIBOCN_FROM=1110006030; XSRF-TOKEN=968285; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO%26uicode%3D10000011%26fid%3D1076036007443584'
}

params = {
    'containerid': '2304136007443584_-_WEIBO_SECOND_PROFILE_WEIBO',
    'page_type': '03'
}

def get_text(url):
    content_list = []
    for page in range(2,10):
        params['page'] = page
        response = requests.get(url,headers=header,params=params).json()
        #print(response['data'])
        time.sleep(0.5)
        data = response.get('data')
        #cards 为list,存储多条相同数据
        cards = data['cards']

        for blog in cards:
            #print(blog)
            #blog 为dict,mblog为字典,判断键是否在字典中
            if 'mblog' in blog:
                mblog = blog['mblog']
                #print(blog['mblog'])
                items = [mblog['text'],mblog['created_at']]
                content_list.append(items)
    print(content_list)
    return  content_list

def save_csv(content_list):
    name = ['text','created_at']
    db = pd.DataFrame(data=content_list,columns=name)
    db.to_csv('data.csv',encoding='utf-8-sig')

if __name__ == '__main__':
    content_list = get_text(url)

    save_csv(content_list)