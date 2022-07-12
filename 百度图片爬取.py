import re
import requests
import os
import time
import random
num = 0
h=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
"Mozilla / 5.0(Macintosh;IntelMacOSX10_7_0) AppleWebKit / 535.11(KHTML, likeGecko) Chrome / 17.0.963.56Safari / 535.11","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"
]
header = {
    'User-Agent': random.choice(h),
    "Cookie":"BIDUPSID=A451FD37266DB03C1EFE2BBDF16FF8E3; PSTM=1641577112; __yjs_duid=1_ca9568f2d0fc51a1a9c085fce1cf8bab1645314386975; MCITY=-289:; BAIDUID=A451FD37266DB03C8445A2DF1E71FB8C:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_31253_34813_36167_34584_36120_36073_36235_26350_36302_36316_36061; delPer=0; PSINO=5; BAIDUID_BFESS=A451FD37266DB03C8445A2DF1E71FB8C:SL=0:NR=10:FG=1; BA_HECTOR=ah2h20048kal2584121h6daoq0q; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1650887030,1650895875; BAIDU_WISE_UID=wapp_1650895875026_837; USER_JUMP=-1; st_key_id=17; video_bubble0=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1650895912; ab_sr=1.0.1_YTkxZjYyNDczN2E5OGIyNWU3N2I4NGZkNmU3N2IxM2Q1ZWYxY2RhY2MyZmM2Y2RiOTVhN2Q4ZTlhNTQxMDI4OWFlN2ExMTc3NzU1YjA1MzE1MTFkNGI4ODhiNDc5M2RmNjZmNTEwZWFlODQ5NGI3MDc4MzAyOGJkNGMyNDdjMjk0OTdmYTRhYWUwNzJlYWUxZWZkMTY4ZmYzNDE2Y2Y5Mg==; st_data=eb963e9ea84b36e0b1ed3a4d43739d037ef1c4f1a1ea53669edcc238f23fd57d013fb4e060e0a8f6d24d4a6695659b9f457a4ceba797e493e667e44cbd59c9493b80149c0d689f006399480d0472dfb8c6d00937d341be3d817e589928615af5; st_sign=95660d30",
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
word=str(input("输入你要爬的内容？："))
n=int(input("要爬几页？："))
page=0
for i in range(n):
    url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&word={word}&pn={page}'

    html = requests.get(url, headers=header,timeout=5)
    html.encoding = 'utf-8'
    html = html.text
    pachong_picture_path = 'C:\\Users\\zzk\\PycharmProjects\\untitled8'
    if not os.path.exists(pachong_picture_path):
        os.mkdir(pachong_picture_path)

    res = re.findall('"objURL":"(.*?)"', html)
    for i in res:
        picture = requests.get(i)
        with open(i.split('/')[-1].split(".")[0]+'.jpg','wb')as f:
            f.write(picture.content)
        print(i.split('/')[-1].split(".")[0]+'.jpg',"下载成功")
    page+=30
    time.sleep(10)
f.close()
