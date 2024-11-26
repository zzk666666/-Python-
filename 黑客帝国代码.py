import pygame,random

pygame.init()
weight=800
height=800
window=pygame.display.set_mode((weight,height))

pygame.display.set_caption("黑客帝国")
window.fill((0,0,0))
bg_face=pygame.Surface((weight,height),flags=pygame.SRCALPHA)#设置一个有透明的画布
bg_face.fill(pygame.Color(0,0,0,23))
font=pygame.font.SysFont('SimHei',22)
jg=22
col=weight//jg
row=height//jg
drops=[]
for i in range(col):
    drops.append(0)
while True:
    window.blit(bg_face, (0, 0))#将透明画布贴在主屏幕上
    for i in range(row):
        r = random.randint(97, 122)
        word = chr(r)
        text=font.render(word, True, (0, 255, 0))
        window.blit(text,(i*col,drops[i]*col))
        drops[i]+=1#字母下落
        if random.random()>0.95:#设置为不整齐下落
            drops[i]=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # 更新渲染
    pygame.display.flip()
    # 减缓下落速度
    pygame.time.delay(50)
