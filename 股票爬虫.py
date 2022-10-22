import requests
from pyecharts.charts import Bar
import pyecharts.options as opts
import re,time
if __name__ == '__main__':
    url_="http://65.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124024051600773740023_1662100517929&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=b:MK0144&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152&_=1662100517930"

    cookies = {
        'qgqp_b_id': 'f50f6df04b7a944ea1da6757de7459c0',
        'st_si': '19634601639704',
        'st_asi': 'delete',
        'st_pvi': '51012516357898',
        'st_sp': '2022-09-02%2014%3A33%3A37',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '3',
        'st_psi': '20220902143411192-113200313001-2277111451',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'qgqp_b_id=f50f6df04b7a944ea1da6757de7459c0; st_si=19634601639704; st_asi=delete; st_pvi=51012516357898; st_sp=2022-09-02%2014%3A33%3A37; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=3; st_psi=20220902143411192-113200313001-2277111451',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    response = requests.get(url_,cookies=cookies, headers=headers, verify=False)

    r=response.text

    res = re.findall('"f14":"(.*?)"', r)
    res2 = re.findall('"f2":\d+\D\d+', r)
    res3 = re.findall('"f3":\d+\D\d+', r)
    name = []
    name2=[]
    newprice = []
    newprice2=[]
    todaychg=[]
    result=[]
    print("名称 最新价 今日涨跌幅")
    for i in range(len(res)):
        name.append(res[i])
        np=re.search('\d+\D\d+', res2[i]).group()
        tc = re.search('\d+\D\d+', res3[i]).group()
        newprice.append(np)
        todaychg.append(tc)
        print(res[i]+":"+np+"\t"+tc+"%")
print(res)
print(newprice)
spc1 = time.strftime("%Y-%m-%d", time.localtime()) + '股价图.html'
spc2 = time.strftime("%Y-%m-%d", time.localtime()) + '涨跌幅图(%).html'




bar = Bar()
bar.add_xaxis(name)
bar.add_yaxis(spc1.replace(".html",""),newprice,itemstyle_opts=opts.ItemStyleOpts(color='blue'))
bar.add_yaxis(spc2.replace(".html",""),todaychg,itemstyle_opts=opts.ItemStyleOpts(color='red'))
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=35),
    ),
    yaxis_opts=opts.AxisOpts(name="价格：（元/股）")
)
bar.render(str(spc1))