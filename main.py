from pygame import *

from random import randint

win_width = 700
win_height = 500

window = display.set_mode((700,500))
display.set_caption('Пинг понг')
window.fill((216, 219, 124))



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
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

game = True
finish = False
ball = GameSprite('ball.png', 300, 200, 50 ,50)
Rocket = Player('Rocket.png', 200, 300, 50, 100)
Rocket1 = Player('Rocket.png', 150, 300, 50, 100)
while game:

    

    for e in event.get():
        if e.type == QUIT:
            game = False

        
    if finish != True:

        ball.update()
        ball.reset()
        Rocket.update()
        Rocket.reset()
        Rocket1.update()
        Rocket1.reset()
        
        display.update()

        time.delay(25)