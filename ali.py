import pygame
import random

lightblue=pygame.Color("lightblue")
purple=pygame.Color("purple")
white=pygame.Color("white")
black=pygame.Color("black")


class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundary_hit=True
        if self.rect.top<0 or self.rect.bottom>=500:
            self.velocity[1]=-self.velocity[1]
            boundary_hit=True

        if boundary_hit:
         pygame.event.post(pygame.event.Event(pygame.USEREVENT+1))
         pygame.event.post(pygame.event.Event(pygame.USEREVENT+2))
    def change_color(self):
        self.image.fill(random.choice([lightblue,purple,white,black]))

def change_bg_():
    global bg_color
    bg_color=random.choice([lightblue,purple,white,black])


allsprite=pygame.sprite.Group()
sp1=Sprite(white,20,30 )
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)


allsprite.add(sp1)

screen=pygame.display.set_mode((500,400))

while True:
    global bg_color
    bg_color=purple
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.fill(bg_color)
    allsprite.update()
    allsprite.draw(screen)
    pygame.display.flip()