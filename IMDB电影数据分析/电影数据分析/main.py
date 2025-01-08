

import requests,random,re

from flask import Flask,render_template,render_template_string,request,redirect,url_for
import openpyxl

import pandas as pd
from pyecharts.charts import Bar,Page,Pie
import pyecharts.options as opts
import math
import numpy as np

from sklearn.linear_model import LinearRegression

import sklearn.linear_model as lm
import matplotlib.pyplot as plt

import os,glob
import shutil
if __name__ == '__main__':
    app = Flask(__name__)

    year=str(input("请输入要分析电影数据的年份"))



    url_ = f"https://www.boxofficemojo.com/year/{year}/?grossesOption=calendarGrosses"

    h = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "UMozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "UsMozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"
    ]
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",

        # 需要登录后的cookie数据
        'cookie': 'session-id=147-3591759-5923855; session-id-time=2082787201l; ubid-main=132-0416991-4415112; session-token=yKYwcVgV1sSi1f5GYK8soabRd3EHrqpW7jXOMVXxNPj6FdfigCs+7DI92AEGuMvQt6BAp29nQsnN4+LS9aHreZosZQtHPUqqDH00556msAO1KcXkLZz795p4dC5zOLI9vOdMI9MST+7Gt96EYjmCfbVvvlw8lVOh+y18Dxdg3i2r5qfE+xAVAvQhHCbvpTsboRv2o6qWOM5ipPoDMcOt1FfGnWJaCtNzSyS6Isv9unRnNCa7U3Md5lu8g99ZWcaY5hcjoVzfI0cyZ07ILEDzjXkzlG/tsSDbBgurz6RCCNrDdcUKOR590Y5ia9Ao8gYgtQ0TUrmTyfj8evMZATm6cg; csm-hit=tb:QCG5PE34NMSDBN8238SQ+b-PEAMBWE0R4SNQGQKJT59|1735404807023&t:1735404807023&adb:adblk_no'
    }
    r = requests.get(url_, headers=header, timeout=5)
    html = r.text
    moive_price = []
    p_str = '<a class="a-link-normal" href="/release/r.*?">(.*?)</a>'
    p_num = '<td class="a-text-right mojo-field-type-money mojo-estimatable">(.*?)</td>'

    moive_name = re.findall(p_str, html, re.S)

    print(moive_name)
    res = re.findall(p_num, html, re.S)
    res_ = []
    #未清洗数据
    for i in range(1, len(res), 2):
        res_.append(res[i])

    print(len(moive_name))
    print(len(res_))
    # 数据清洗
    for i in res_:
        x = str(i).replace('$', '')

        moive_price.append(int(x.replace(',', '')))
    print(moive_price)
    avg_price = sum(moive_price) / len(moive_price)
    data = []
    #将爬取下来的数据保存为excel
    j = 0
    for i in moive_name:
        data.append([i, moive_price[j]])
        j += 1
    df = pd.DataFrame(data, columns=['name', 'price'])
    if os.path.exists(f"{year}年IMDB电影票房数据可视化.xlsx"):
        os.remove(f"{year}年IMDB电影票房数据可视化.xlsx")
        df.to_excel(f"{year}年IMDB电影票房数据可视化.xlsx")
    else:
        df.to_excel(f"{year}年IMDB电影票房数据可视化.xlsx")




    X = np.array(moive_price).reshape(-1,1)
    b=1

    noise = np.random.uniform(-2, 2)

    y= 5*X+b+noise

    lr=LinearRegression()
    lr.fit(np.reshape(X,(-1,1)),np.reshape(y,(-1,1)))
    y_pred = lr.predict(X)
    plt.figure(figsize=(5, 5))
    plt.scatter(X, y)  # 画散点图
    plt.plot(X, y_pred, color='red')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel("电影票房样本(亿)")
    plt.ylabel("损失")
    plt.title(f"{year}年年IMDB电影票房数据模型")
    plt.savefig(f'static/{year}年数据模型.png')
    plt.show()
    mes="The linear model is: Y = {:.5} + {:.5}X".format(lr.intercept_[0], lr.coef_[0][0])




    

    @app.route('/')
    def index():
        # show_data=render_template_string(open('templates/show_data.html').read(),moive_name=moive_name,moive_price=res_)

        piaofang = render_template('票房.html')
        return piaofang


    @app.route('/show_data.html')
    def show_data():
        # show_data=render_template_string(open('templates/show_data.html').read(),moive_name=moive_name,moive_price=res_)

        showdata = render_template('show_data.html', moive_name=moive_name, moive_price=res_,year=year)
        return showdata


    @app.route('/data_cleaning.html')
    def data_cleaning():
        # show_data=render_template_string(open('templates/show_data.html').read(),moive_name=moive_name,moive_price=res_)

        datacleaning = render_template('data_cleaning.html', moive_name=moive_name, moive_price=moive_price,year=year)
        return datacleaning


    @app.route('/电影票房数据分析.html')
    def data_analysis():
        # show_data=render_template_string(open('templates/show_data.html').read(),moive_name=moive_name,moive_price=res_)

        dataanalysis = render_template('电影票房数据分析.html',year=year)
        return dataanalysis




    @app.route('/票房.html')
    def shouye():
        # show_data=render_template_string(open('templates/show_data.html').read(),moive_name=moive_name,moive_price=res_)

        piaofang = render_template('票房.html')
        return piaofang


    image_folder = 'static'
    images = os.listdir(image_folder)
    images = [img for img in images if img.endswith(('.jpg', 'png', '.gif'))]
    @app.route('/data_model.html')
    def data_model():
        # image_folder='static'
        # images=os.listdir(image_folder)
        # images=[img for img in images if img.endswith(('.jpg','png','.gif'))]

        datamodel = render_template('data_model.html',images=images,year=year)
        return datamodel


    @app.route("/电影票房数据可视化.html")
    def data_analysis_1():
        # show_data=render_template_string(open('templates/show_data.html').read(),moive_name=moive_name,moive_price=res_)

        dataanalysis = render_template("电影票房数据可视化.html")
        return dataanalysis



    # @app.route('/upload',methods=['GET','POST'])
    # def upload():
    #     if request.method=="POST":
    #         image_file=request.files['image']
    #         if image_file:
    #             ImageManager.upload_image(image_file)
    #]]]]]]
    #             return redirect(url_for('index'))
    #     return render_template('')

    #数据可视化
    #柱形图
    page = Page()
    bar = Bar()
    bar.add_xaxis(moive_name)

    bar.add_yaxis("票房", moive_price, itemstyle_opts=opts.ItemStyleOpts(color='red'))
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title=f"{year}年IMDB票房数据可视化柱形图"),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=35),
        ),
        yaxis_opts=opts.AxisOpts(name="票房")
    )
    page.add(bar)
    # 饼图
    pie = (
        Pie()
            .add(f'{year}年票房数据可视化饼图', [(i, j) for i, j in zip(moive_name, moive_price)], center=["50%", "50%"],
                 radius=[0, 100])
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{year}年票房数据可视化饼图"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    page.add(pie)

    page.render("templates/电影票房数据可视化.html")
    app.run(debug=True, host='0.0.0.0', port=25000)
    folder_path = "static"
    for file_name in os.listdir(folder_path):

        if file_name.endswith('.png'):
            os.remove(f"{folder_path}/{file_name}")

            #return Markup(page.render_embed())


    # for i in res:
    #     print(i)
    #     p_str='<a class="a-link-normal mojo-truncate aok-block" href="/release/r.*?">(.*?)</a>'
    #     r=re.findall(p_str,i,re.S)
    #     print(r)