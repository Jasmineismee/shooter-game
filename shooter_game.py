#Create your own shooter


from pygame import *
from random import randint


window_width = 1200
window_height = 800




#FONT and caption
font.init()
font1 = font.Font(None, 80)
win  = font1.render("You win", True, (255,255,255))  #kêu font1 tạo chữ You win có màu (255,255,255) rồi bỏ vào biến win
lose  = font1.render("You lose", True, (176,95,50))
font2 = font.Font(None, 80)


# image variable
background_img = 'galaxy.jpg'
img_enemy = "ufo.png"
player_img = "rocket.png"
bullet_img = "bullet.png"


# game variable
score = 0
lost = 0
max_lost = 3


window = display.set_mode((window_width,window_height))
display.set_caption("Shooter")
#background
background = transform.scale(image.load(background_img), (window_width,window_height))


#class
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))


#player class
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed


    def shoot(self):
        bullet = Bullet(bullet_img, self.rect.centerx, self.rect.top, 15,20,15)
        bullets.add(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed  # + - 15 ddi leen
        if self.rect.y < 0:
            self.kill()
         


#enemy class
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost


        if self.rect.y > window_height:   # di qua 800 px
            self.rect.y = 0
            self.rect.x = randint(80,window_width -80)
            lost +=1


#Create game object


ship = Player(player_img, 5, 200,80, 100, 10)




monsters = sprite.Group()
bullets = sprite.Group()
for i in range(1,6):
    monster = Enemy(img_enemy, randint(80, window_width-80),-40, 80, 50, 5)
    monsters.add(monster)






#Variables
finish = False  #1
clock = time.Clock()
FPS = 60
run = True   #2




while run:    #3
    for e in event.get():
        if e.type == QUIT:
            run = False  #4
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.shoot()


    if not finish:
        window.blit(background,(0,0))


        #write text on screen
        text = font2.render("Score:" + str(score), 1, (255,255,255) )
        window.blit(text, (10,20))


        missed = font2.render("Missed:" + str(lost), 1, (255,255,255) )
        window.blit(missed, (10,50))


        ship.update()
        monsters.update()
        bullets.update()




        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
       


        display.update()
        clock.tick(FPS)
