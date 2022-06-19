#-*- encoding:utf-8 -*-
import random,os
from threading import Thread
import tqdm
import time
team1=["毕宿五星空骑士","Gliese 581g星空骑士","孤勇者","甜柠檬"]
team2=["开哥","骚猪","HAPE","新津天皇","NM$L","葛平","大司马","洪世贤"]
abuse_word1=["叶宇轩是贱逼、叶宇轩欺负女人不要脸","打的叶宇轩狗不吃叶宇轩","电锯惊魂来叶宇轩家了","瘦长鬼影使叶宇轩发高烧最后离奇失踪","我自横刀向天笑，去留肝胆两昆仑！","君子报仇十年不晚，有恩报恩有仇报仇","此头须向国门悬，必杀叶（指叶宇轩的兵）家军十万！","叶宇轩不小心进了游戏遭遇头号玩家的轮番攻击","叶宇轩去了火葬场火化","把叶宇轩分尸、碎石、再烹尸！","把叶宇轩骨灰扔进日本海里","叶宇轩根本没有钱，因为他的钱拿去嫖娼了","震惊！叶宇轩猥亵香山中学（高中部）校长的女儿","叶宇轩四季如春（一年四季发春）","叶宇轩去大日本帝国拍av吧","叶宇轩祖坟爆炸"]
abuse_word2=["叶宇轩的包皮被卖","叶宇轩是没有包皮","叶宇轩傻逼","叶宇轩智障","叶宇轩死妈","叶宇轩被割包皮","干你妈的叶宇轩家的iPhone*（*代表所有系列）","武士刀劈死叶宇轩","把叶宇轩抓进三体，让三体人用指令使他消失！","兄弟们为初中往事尽情的骂！","叶宇轩躺进棺材里头","把叶宇轩骨灰扔进恒河水里","宇宙的厚度是叶宇轩∞分之一光年","以后生女儿遇到叶宇轩要小心","叶宇轩的没有钱，因为钱都掉棺材里头了！","叶宇轩一触即发"]
laladui=["加油","加油！奥利给","奥利给","奥力干","冲冲冲"]
for i in tqdm.tqdm(range(100)):
    time.sleep(0.1)
def yyx1(q,name):
    for i in range(1000):
        print(f"({q}){name}：{random.choice(abuse_word1)}|")
        time.sleep(1)
    time.sleep(6)
    time.sleep(6)
    print("发泄完毕，立即关机！")
    os.system('shutdown -s -t 10')
def yyx2(q,name):
    for i in range(1000):
        print(f"({q}){name}：{random.choice(abuse_word2)}|")
        time.sleep(1)
    time.sleep(6)
    print("发泄完毕，立即关机！")
    os.system('shutdown -s -t 10')
def guangzhong(q):
    for i in range(1000):
        print(f"({q})观众：{random.choice(laladui)}|")
        res=random.randint(1,1000)
        if res==666 or res==444:
            print("叶宇轩的祖坟爆炸，棺材被炸开，尸体灰飞烟灭！奥利给！")
        time.sleep(1)
    time.sleep(6)
    os.system('shutdown -s -t 10')
if __name__=='__main__':
    name1=random.choice(team1)
    name2 = random.choice(team2)
    t1=Thread(target=yyx1,args=(1,),kwargs={"name":name1})
    t2 = Thread(target=yyx2, args=(2,),kwargs={"name":name2})
    t3 = Thread(target=guangzhong, args=(3,))
    print("大家好！这里是由肯德基冠名播出的有仇必报节目，我是主持人李天昊。今天3000多人来观看这场比赛，观众的心情都是欣喜若狂，不知道今天的比赛是哪一战队呢？大家拭目以待！")
    print(f"由请{name1}战队登场")
    print(f"由请{name2}战队登场")
    print(f"大家好我是{name1}战队我是第一个出场，我是（1）大家记住我的编号")
    print(f"大家好我是{name2}战队我是我第二个出场，我是（2）大家记住我的编号")
    print("注：（3）代表起哄的观众")
    time.sleep(3)
    t1.start()
    t2.start()
    t3.start()