from pygame import *

from random import randint

win_width = 700
win_height = 500

window = display.set_mode((700,500))
display.set_caption('Пинг понг')
window.fill((216, 219, 124))

speed_x = 3
speed_y = 3



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
           self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
           self.rect.y += self.speed

game = True
finish = False
ball = GameSprite('ball.png', 325, 200, 4, 50 ,50)
Rocket = Player('Rocket.png', 50, 200, 4, 50, 100)
Rocket1 = Player('Rocket.png', 600, 200, 4, 50, 100)

while game:

    

    for e in event.get():
        if e.type == QUIT:
            game = False

        
    if finish != True:


        window.fill((216, 219, 124))

        ball.update()
        ball.reset()
        Rocket.update_l()
        Rocket.reset()
        Rocket1.update_r()
        Rocket1.reset()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(Rocket, ball) or sprite.collide_rect(Rocket1, ball):

            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:

            speed_y *= -1
        display.update()

        time.delay(25)
