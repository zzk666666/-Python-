from selenium import webdriver
import time
import random
if __name__=='__main__':
    search_=["咒怨","毛毛虫","空手指","下水道的美人鱼","杀手杰夫","朱秀华","红衣男孩","松毛虫","跳水失败"]
    chrome_obj=webdriver.Chrome()
    for i in range(100):
        chrome_obj.get('https://image.baidu.com/')
        time.sleep(5)
        input_obj=chrome_obj.find_element_by_id('kw')
        input_obj.send_keys(random.choice(search_))
        click_obj = chrome_obj.find_element_by_class_name('s_newBtn')
        click_obj.click()