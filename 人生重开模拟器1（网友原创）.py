#-*- encoding:utf-8 -*-
from multiprocessing import Manager
import random,asyncio,time
C=100
semaphone=asyncio.Semaphore(C)
tasks=[]
async def GetResponse(sum3,i):
    async with semaphone:
        print(f"{sum3}岁 {i}")
        await asyncio.sleep(1)
async def funa(sum3,i):
    await GetResponse(sum3,i)
class yourlife(object):

    def __init__(self):
        self.init=["0岁你出生了是个男孩","1岁你自学会了走路","2岁你学会了数独","3岁上了城里的幼儿园","4岁你学完了Python","5岁你学会C++、Java。","6岁你上了城里的普通小学","7岁你为班级同学写了表白程序，你父母没说你早恋。","8岁你因为调戏了你10岁的姐姐被父母第一次打","9岁你第一次学会3D建模","10岁你学会Mysql数据库","11岁你和同学一起出去吃饭","12岁你上了国际学校（初中）","13岁由于老外出言不逊调侃中国你看不下去了黑了他的电脑","14岁你出国上了私立中学","15岁因为老师调戏中国女学生，你黑掉老师的Facebook和Whatsapp","16岁你被学校称为电脑怪才，逃课编程","17岁你写了一款游戏卖了1亿","18岁你上了大学","19岁你有了自己的车","20岁你结婚了","21岁你回国生孩子","22岁你身高193"]

        self.younth=["塔利班组织闪击波兰,法国宣布投降。","日本武力攻占珍珠港","在云南发现太岁肉芝价值1兆","探险队在昆仑山发现九尾狐还会发光","中国经济超过美国","教育局宣布提倡中学生早恋","上海小学生春游登顶珠峰","你非常热爱你的工作，老板也觉得你善良。","上海新闻频道报道上海杨浦小学生神秘失踪事件，被发现已经像被妖怪吸走精气。","美国发现超人","乌克兰占领莫斯科","苏联再次合体","日本再次占领中国","日本占领加州","中国已是全球第一经济体","江苏省省会改名苏州","解放军武力占领东京","台湾回归，一国三制开始实行。"]

        self.Middle_aged=["你儿子在班里被女同学欺负，你儿子反击抓了她的敏感部位，被叫去德育处。","朝鲜统一韩国","新闻联播在四川某地发现神秘生物疑似女鬼","你成为本世纪科技人物","你做噩梦梦见中学时老师打你","小学课本已经出现物理","啥也没发生","中国改国号中华帝国被国际承认","塔利班占领华盛顿","埃塞俄比亚经济直逼中国","上海超群大厦竣工高度10000米超越珠穆朗玛峰","你女儿吃烧烤遇到猥琐男，女儿用空手道击退对方，并一打10。","南京发现日本兵的鬼魂，被人群殴。","港澳台允许服兵役","肯德基加入清真食品","CNN报道本拉登未被击毙，潜伏在巴基斯坦准备筹划再次袭击美国本土","卢本伟当了慈善家","朝鲜对外开放","中国可以允许浏览外网已经社交软件","天皇承认侵华战争并引起左派众怒，左派推翻天皇建立社会主义日本。","神农架野人进城"]

        self.old_aged=["中小学生寒暑假作业改作文作业","山东4米高的巨人老张","教育局规定中小学午休强制让学生休眠（除高三）","高考分数线降低","你在骑行的时候差点摔进悬崖，狐仙现身救了你。","中国与美国通高速公路","日本承认731部队对华犯下滔天罪行","新疆发现霸王龙袭击解放军兵团，后被证实是真的。","中小学严打校园欺凌","靖国神社被当做奇葩旅游景点，进去需踩踏日本国旗。","中国恢复共产主义帝制且有实权","平平淡淡，没有什么特别的事。","艾滋病已被治愈","近视已经可以轻松治愈","你父亲去世","你母亲去世","你们全家欧洲游","上海平均身高超过山东","中国男性平均身高190","中国女性平均身高175","新法律喷子必须死刑","取消补习班","学校取消晚自习（并且晚自习要发老师款）","法律老师禁止体罚学生","美国修改小学入学年龄为10到12岁","专家推测由于海平面的升高，日本可能在20年后沉没。","你们全家去了东南亚旅游","你们全家去了非洲旅游","中国养老福利超过日本美国","狂犬病已被治愈","你像黄延秋一样被外星人背着飞了大半个中国，但最后你活着回来了。","你的孙子早恋了，你没有生气还夸孙子。","性教育已经被纳入幼儿园课程","印度已经成为联合国常任理事国六常"]

        self.death=["重重的摔了一跤","你被车撞死了","你在国外被枪击死"]

        self.deathofbaby=["你胎死腹中","你被父母故意摔在地上","你妈因为早孕你外公外婆叫你妈把你被打掉了","你妈不想要你直接打胎","你妈堕胎了"]

        self.length1 = len(self.younth)

        self.length2 = len(self.Middle_aged)

        self.length3 = len(self.old_aged)

        self.sum1=0

        self.sum2=23

        self.sum3=60

        self.r = random.randint(0, 22)

        self.r1 = random.randint(23, 100)

        self.r2 = random.randint(30, 100)

        self.r3 = random.randint(60, 100)

        self.r4 = random.randint(81, 10000)


    def before(self,q):
            for i in self.init:
                q.put(i)
            for i in self.init:
                if self.sum1 == self.r:
                    if self.r == 0:
                        print(random.choice(self.deathofbaby))
                        break
                    else:
                        print(f"{self.sum1}岁 {random.choice(self.death)}")
                        break
                else:
                    print(q.get(i))
                time.sleep(1)
    def addofafter(self):
        after1=[]
        after2 = []
        after3 = []
        for i in range(self.length1):
            after1.append(random.choice(self.younth))
        for i in range(self.length2):
            after2.append(random.choice(self.Middle_aged))
        for i in range(self.length3):
            after3.append(random.choice(self.old_aged))
        global l1,l2,l3
        l1 = set(after1)
        l2 = set(after2)
        l3 = set(after3)
    def after(self):
        for i in l1:
            if self.sum2 == self.r1:
                print(f"{self.sum2}岁 {random.choice(self.death)}")
                break
            else:
                print(f"{self.sum2}岁 {i}")
                time.sleep(1)
            self.sum1 += 1
        for i in l2:
            if self.sum2 == self.r2:
                print(f"{self.sum2}岁 {random.choice(self.death)}")
                break
            else:
                print(f"{self.sum2}岁 {i}")
                time.sleep(1)
            self.sum2 += 1
        for i in l3:
            if self.sum3 == self.r3:
                print(f"{self.sum3}岁 {random.choice(self.death)}")
                break
            else:
                print(f"{self.sum3}岁 {i}")
                time.sleep(1)
            self.sum3 += 1
    def Monasticism(self):
        for i in range(self.r4):
            task = asyncio.ensure_future(funa(self.sum3, "修仙"))
            self.sum3 += 1
            tasks.append(task)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        return f"{self.sum3}岁你渡劫失败，你被雷劈死了。"
if __name__ == '__main__':
    q = Manager().Queue()
    yl=yourlife()
    yl.before(q)
    yl.addofafter()
    yl.after()
    yl.Monasticism()
