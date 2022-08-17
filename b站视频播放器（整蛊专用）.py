import requests
import time
import jsonpath
import random
from selenium import webdriver
import re
if __name__=='__main__':
    data_=input("请输入您想播放的视频")
    page_ = input("请输入播放第几页")
    page_=re.match("\d*",page_).group()
    chrome_obj = webdriver.Chrome()
    url_ = "https://api.bilibili.com/x/web-interface/search/all/v2"
    page=24
    for i in range(int(page_)):
        headers_ = {
            "referer": f"https://search.bilibili.com/all?keyword={data_}&from_source=webtop_search&spm_id_from=333.1007".encode('utf-8').decode('latin1'),
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
            "Cookie": "BIDUPSID=A451FD37266DB03C1EFE2BBDF16FF8E3; PSTM=1641577112; __yjs_duid=1_ca9568f2d0fc51a1a9c085fce1cf8bab1645314386975; MCITY=-289:; BAIDUID=A451FD37266DB03C8445A2DF1E71FB8C:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_31253_34813_36167_34584_36120_36073_36235_26350_36302_36316_36061; delPer=0; PSINO=5; BAIDUID_BFESS=A451FD37266DB03C8445A2DF1E71FB8C:SL=0:NR=10:FG=1; BA_HECTOR=ah2h20048kal2584121h6daoq0q; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1650887030,1650895875; BAIDU_WISE_UID=wapp_1650895875026_837; USER_JUMP=-1; st_key_id=17; video_bubble0=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1650895912; ab_sr=1.0.1_YTkxZjYyNDczN2E5OGIyNWU3N2I4NGZkNmU3N2IxM2Q1ZWYxY2RhY2MyZmM2Y2RiOTVhN2Q4ZTlhNTQxMDI4OWFlN2ExMTc3NzU1YjA1MzE1MTFkNGI4ODhiNDc5M2RmNjZmNTEwZWFlODQ5NGI3MDc4MzAyOGJkNGMyNDdjMjk0OTdmYTRhYWUwNzJlYWUxZWZkMTY4ZmYzNDE2Y2Y5Mg==; st_data=eb963e9ea84b36e0b1ed3a4d43739d037ef1c4f1a1ea53669edcc238f23fd57d013fb4e060e0a8f6d24d4a6695659b9f457a4ceba797e493e667e44cbd59c9493b80149c0d689f006399480d0472dfb8c6d00937d341be3d817e589928615af5; st_sign=95660d30"
        }
        params_ = {
            "__refresh__": "true",
            "_extra":"",
            "context":"",
            "page": str(i+1),
            "page_size":"30",
            "from_source":"",
            "from_spmid": "333.337",
            "platform":"pc",
            "highlight":"1",
            "single_column":"0",
            "keyword":str(data_),
            "category_id":"",
            "search_type": "video",
            "dynamic_offset":str(page*i),
            "preload": "true",
            "com2co": "true"
        }

        response_ = requests.get(url_, headers=headers_, params=params_)
        data=response_.text
        print(data)
        py_data = response_.json()
        url_list = jsonpath.jsonpath(py_data, '$..arcurl')
        print(len(url_list), url_list)
        chrome_obj.get(random.choice(url_list))
        chrome_obj.maximize_window()
        time.sleep(random.uniform(0.1,60.0))
