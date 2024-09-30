# This is a sample Python script.
#导入正则库
import re
#导入请求模块，用于请求网页。
import requests

import random#导入随机模块，随机选择用户代理。

from wordcloud import WordCloud#导入词云图模块，用于生成评论。
from collections import Counter#选择组合模块里的Counter模块来统计词频

from pyecharts.charts import Bar#数据可视化模块pyecharts里的柱形图
from PIL import Image
import pyecharts.options as opts#配置项类名
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #用户代理列表
    h = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "UMozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "UsMozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"
    ]
    # cookies数据
    cookies = {
        'cookie2': '13b738f06873812a5e1f5d9968087966',
        '_m_h5_tk': '4435d4c0f66d847969e770a69089c5bc_1715612625436',
        '_m_h5_tk_enc': 'e55589bb7b650e12796658d9dafb6e91',
        'sgcookie': 'E100V2ayyMYY4bkQFZdJiDw40m3v5xhgE8OBleeOVVNWsKZbEL2nfx50Lt%2FXb0IMJnhEYSh1PNLEGVSMbCFxRlARNUTFkRryYz7UMKbkQqZ3fHCjSUUV95shb6%2F3KJCbd6fr',
    }


    #关键词列表
    report_words1 = []
    #获取目标url
    url_ = "https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.2&appKey=12574478&t=1717338399888&sign=69fd0d026cac23e9e16305b6173f2341&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=10000&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&dataType=json&valueType=string&preventFallback=true&type=json&data=%7B%22itemId%22%3A%2215257702935%22%2C%22bizCode%22%3A%22ali.china.tmall%22%2C%22channel%22%3A%22pc_detail%22%2C%22pageSize%22%3A20%2C%22pageNum%22%3A1%7D"
    #请求头
    headers = {
        "User-Agent": random.choice(h),
        # 需要登录后的cookie数据
        'cookie': 'cna=GibRHaAsMFwCAbSg+8nM+U5/; lid=%E7%BA%A2%E7%8A%BC%E4%B9%90%E9%98%9F%E4%B8%BB%E5%94%B1; miid=200082981355829654; wk_unb=UNk%2BeBAc0q7BGg%3D%3D; wk_cookie2=16e8c4e621ece319813af8894dd7cb23; dnk=%5Cu7EA2%5Cu72BC%5Cu4E50%5Cu961F%5Cu4E3B%5Cu5531; tracknick=%5Cu7EA2%5Cu72BC%5Cu4E50%5Cu961F%5Cu4E3B%5Cu5531; lgc=%5Cu7EA2%5Cu72BC%5Cu4E50%5Cu961F%5Cu4E3B%5Cu5531; cookie2=21f17ad8a0b70c4affb8b01fb0a3e55b; t=b7a6740abfef6bb6cf6203e4004c9b42; sn=; _tb_token_=1eeb84a6138b; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=a10dc57803c78f42dd0ac0d3cdc30c9d_1717345078780; _m_h5_tk_enc=98bb19c2618fce09583419d30e0eae95; _l_g_=Ug%3D%3D; cookie3_bak=21f17ad8a0b70c4affb8b01fb0a3e55b; cookie1=UIH3eFhwEAINPFjkCwTT7Nh2nIAK0P0lyHVihgrCxMg%3D; login=true; env_bak=FM%2BgzJsXjLR5NWkeeeikXzn5imwifJ1xjfyPVx36Dc2G; cancelledSubSites=empty; sg=%E5%94%B121; uc1=cookie15=VT5L2FSpMGV7TQ%3D%3D&pas=0&existShop=false&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UtASsssme%2BBq&cookie14=UoYfpuK%2F9PbdCA%3D%3D; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3eK8vFfI%2Bmcj0ss%3D&id2=UNk%2BeBAc0q7BGg%3D%3D&nk2=2UzGa3xangYv5X2%2B; uc4=id4=0%40Ug40ebci8TbZYX4WaHT4evgMvVj5&nk4=0%4026qgRXhGcpy67GZHtCWmyYoIRGMjXMk%3D; unb=3995157682; cookie17=UNk%2BeBAc0q7BGg%3D%3D; _nk_=%5Cu7EA2%5Cu72BC%5Cu4E50%5Cu961F%5Cu4E3B%5Cu5531; sgcookie=E1001XR2%2BzBppNV3%2FNCzn%2Fzb54u0O%2FCtxXkMY5U%2BFOoW3Z2L%2BYvadSEDRWlQgsxldKPh%2FuH94bgZ0oN3dCwsw%2B78O2PdswnkK3VtN0N28HyDwS945SLaJtCG%2FUcnCwB94ZB8; csg=4cf01ef1; cookie3_bak_exp=1717597100154; tfstk=f5ktQaAJseYgiIAmCcOnuLcZO1tn6AnwpVo5nr4GG23KlVtaSPDDHX3rytxZsqcLc20Yn-mX7qHYRVBmscmfDog3CSlgoP4YHmuJxUvkEcoa3RTkrL4pPcj4UoabcZ2QduQtRfhJEcoNAGQXqX9lMHv0TAajl5NIAozQf1NslJwQby6_cOZfRHE4Rrwb5S_CdoEAGsZf1jXJ6rY3ztHHNqH8MUrdhtM635U-usXAHvET6rogJkqnplFTPWmvYFHs-mMiQWRC9-onwqhjPefg5bE-J7c9yO3-7ogQAVxcgkhxcYya6gXovSUtOANdctiLpPNmMVLO_PGiJ7rQOipzx44IbAGp0wisrPe_AWvW2DNjtAPrIe6TFbogIjgW-14swosyXYDJbAQuyof6vHCVg5Z3R6gHzIzPhUqLrHxhgsPKWkUkvHCVg5ZUvzxEzs549VC..; isg=BPDwJt_FYq8nEj62N-97eJ2awb5COdSD5-f7TupBoMsFpZFPkklqEzLT_a3FVoxb',
        'Referer': 'https://chaoshi.detail.tmall.com/'
    }
    #页面参数
    params = {
        'sv': '2.7.2',
        'appKey': '12574478',
        't': '1717339103163',
        'sign': '6fe32890bf7fd3bc53ed3e640d6432d3',
        'api': 'mtop.alibaba.review.list.for.new.pc.detail',
        'v': '1.0',
        'isSec': '0',
        'ecode': '0',
        'timeout': '10000',
        'ttid': '2022@taobao_litepc_9.17.0',
        'AntiFlood': 'true',
        'AntiCreep': 'true',
        'dataType': 'json',
        'valueType': 'string',
        'preventFallback': 'true',
        'type': 'json',
        'data': {"itemId":"15257702935","bizCode":"ali.china.tmall","channel":"pc_detail","pageSize":20,"pageNum":1}

    }
    r = requests.get(url_, headers=headers, params=params,timeout=10)
    article = r.text#获取网页内容
    p_article = '"reviewWordContent":"(.*?)",' #(.*?)代表获取子字符串
    article_main = re.findall(p_article, article)#匹配关键字符串
    print(article)
    triangle=Image.open('微信图片_20240602222523.png')
    square = Image.open('微信图片_20240602222532.png')
    #circle= Image.open('微信图片_20240602225034.png')
    China = Image.open('微信图片_20240602222538.png')
    mask_triangle=np.array(triangle)
    mask_square = np.array(square)
    #mask_circle = np.array(circle)
    mask_China = np.array(China)



    with open("娃哈哈AD钙奶评论.txt",'w',encoding='utf-8') as f:
        for i in article_main:
            f.write(i)
    for i in article_main:
        if len(i)>=4:
            report_words1.append(i)
    content=' '.join(report_words1)#连接关键词
    content.encode('utf-8')
    triangle_wc=WordCloud(font_path='simsun.ttc',mask=mask_triangle,background_color='white',width=1000,height=600).generate(content)
    triangle_wc.to_file('AD钙奶评论词云图1（淘宝）.png')#生成词云图

    square_wc = WordCloud(font_path='simsun.ttc', mask=mask_square, background_color='white', width=1000,
                            height=600).generate(content)
    square_wc.to_file('AD钙奶评论词云图2（淘宝）.png')  # 生成词云图

    #circle_wc = WordCloud(font_path='simsun.ttc', mask=mask_circle, background_color='white', width=1000,
#                          height=600).generate(content)
    #circle_wc.to_file('AD钙奶评论词云图3（淘宝）.png')  # 生成词云图

    China_wc = WordCloud(font_path='simsun.ttc', mask=mask_China, background_color='white', width=1000,
                          height=600).generate(content)
    China_wc.to_file('AD钙奶评论词云图3（淘宝）.png')  # 生成词云图


    result1=Counter(report_words1).most_common(10)#获取词频前10的词
    #使用冒牌排序（升序）排序词频
    for i in range(1,len(result1)):
        for j in range(1,len(result1)):
            if result1[j-1][1]<result1[j][1]:
                result1[j-1]=result1[j]

    print(result1)

    r1=[]#关键词名称
    r1_=[]#关键词词频

    for i in range(len(result1)):
        r1.append(result1[i][0])
        r1_.append(result1[i][1])

    bar=Bar()#柱形图
    bar.add_xaxis(r1)#x轴数据
    bar.add_yaxis("娃哈哈AD钙奶评论前10的词",r1_,itemstyle_opts=opts.ItemStyleOpts(color='blue'))#y轴数据
    #xaxis_opts为x轴配置项属性 axislabel_opts为标签配置属性 rotate=35为逆时针旋转35
    bar.set_global_opts(
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=35),
        ),
        yaxis_opts=opts.AxisOpts(name="词频（term frequency，TF）")
    )
    bar.render("娃哈哈AD钙奶评论前10的词.html")#渲染生成可视化数据，文件格式为html。



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
