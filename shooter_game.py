#Моя первая попытка

'''from pygame import *
from random import randint



mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font2 = font.Font(None, 36)

img_back = "galaxy.jpg"
img_hero = "400px-Jotaro_SC_Infobox_Manga.png"
img_enemy = "dio_sc_2.webp"
img_bullet = "bullet.png"

win_width = 800
win_height = 600
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

bullets = sprite.Group()



score = 0
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("Без названия.jpg", self.rect.centerx, self.rect.top, 70, 100, -15)
        bullets.add(bullet)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1


player = Player(img_hero, 5, win_height - 100, 80, 100, 20)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("dio_sc_2.webp", randint(80, win_width - 80), -40, 60, 100, randint(1, 15))
    monsters.add(monster)
FPS = 60
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()
    if not finish:
        window.blit(background,(0,0))
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        player.update()
        monsters.update()
        player.reset()
        bullets.update()
        monsters.draw(window)
        bullets.draw(window)
       
    
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1 
            monster = Enemy("dio_sc_2.webp", randint(80, win_width - 80), -40, 50, 100, randint(1, 5))
            monsters.add(monster)
        display.update()
    time.delay(50)'''
#Моя пределанная игра
from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 36)
win = font1.render('YOU WIN', True, (0, 255, 0))
lose = font2.render('YOU LOSE', True, (255, 0, 0))

mixer.init()
mixer.music.load('jojos-golden-wind.mp3')
mixer.music.play()
fire_sound = mixer.Sound('star-platinum-za-warudo.mp3')

img_back = 'San_Giorgio_Maggiore_island_manga.png '
img_hero = "400px-Jotaro_SC_Infobox_Manga.png"
img_enemy = "dio_sc_2.webp"
img_bullet = "Star_Platinum_SO_Infobox_Anime.webp"

score = 0
goal = 30
lost = 0
max_lost = 1

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 70, 100, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 800
win_height = 600
display.set_caption("Невероятные пиключение ДжоДжо, Dio vs Jotaro")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

player = Player(img_hero, 5, win_height - 100, 80, 100, 25)
 
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("dio_sc_2.webp", randint(80, win_width - 80), -40, 80, 100, randint(1, 15))
    monsters.add(monster)
bullets = sprite.Group()
FPS = 60
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()
    if not finish:
        window.blit(background,(0,0))
        player.update()
        monsters.update()
        player.reset()
        bullets.update()
        monsters.draw(window)
        bullets.draw(window)

        text = font2.render("Счет: " + str(score), 1, (0, 255, 0))
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено: " + str(lost), 1, (0, 0, 255))
        window.blit(text_lose, (10, 50))
       
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 100, randint(1, 15))
            monsters.add(monster)

        if sprite.spritecollide(player, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

        if score >= goal:
            finish = True
            window.blit(win, (200, 200))  
        display.update()  
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)      
        for i in range(1, 6):
            monster = Enemy("dio_sc_2.webp", randint(80, win_width - 80), -40, 80, 100, randint(1, 15))
            monsters.add(monster)


        
    time.delay(50) 