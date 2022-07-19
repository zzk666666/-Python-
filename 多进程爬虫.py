import requests
import multiprocessing
result=[]
url="//scpic.chinaz.net/Files/pic/pic9/202206/hpic5521_s.jpg"
def GetResponse(url,queue):
    queue.put(url)
    response_=requests.get(url,headers="'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'")
    data=response_.content
    with open(url.split('/')[-1].split(".")[0]+'.jpg','wb')as f:
        f.write(data)
    return data
if __name__ == '__main__':
    url = "https://scpic.chinaz.net/Files/pic/pic9/202206/hpic5521_s.jpg"
    queue=multiprocessing.Queue()
    p=multiprocessing.Process(target=GetResponse,args=(url,queue))
    p.start()
