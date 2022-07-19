import requests
from retrying import retry
from retrying import retry
class Baidu:
    def __init__(self):
        self.url_="https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsNiwxLDUsNCw4LDcsOQ%3D%3D&word=%E5%92%92%E6%80%A8"
        self.num_=0
    @retry(stop_max_attempt_number=3) #最大重试次数
    def send_requset(self):
        self.num_+=1
        print(self.num_)
        requests.get(self.url_)
    def run(self):
        try:
            self.send_requset()
        except Exception as e:
            print(e)
if __name__=="__main__":
    url_="https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsNiwxLDUsNCw4LDcsOQ%3D%3D&word=%E5%92%92%E6%80%A8"
    headers_={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    proxies_={"http":"http://192.168.1.10:54396"} #ip地址与端口号
    response_=requests.get(url_,headers=headers_,proxies=proxies_,timeout=3)
    str_data=response_.content.decode()
    print(str_data)
