import pygame
import random
pygame.init()
WIDTH, HEIGHT=800, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Changing Sprites")
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.Surface((60, 60))
        self.color=random_color()
        self.image.fill(self.color)
        self.rect=self.image.get_rect(center=(x, y))
    def change_color(self):
        self.color=random_color()
        self.image.fill(self.color)
sprite1=ColorSprite(200, 300)
sprite2=ColorSprite(600, 300)
all_sprites=pygame.sprite.Group(sprite1, sprite2)
COLOR_CHANGE_EVENT=pygame.USEREVENT+1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000)
clock=pygame.time.Clock()
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==COLOR_CHANGE_EVENT:
            for sprite in all_sprites:
                sprite.change_color()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        sprite1.rect.x-=5
    if keys[pygame.K_d]:
        sprite1.rect.x+=5
    if keys[pygame.K_LEFT]:
        sprite2.rect.x-=5
    if keys[pygame.K_RIGHT]:
        sprite2.rect.x+=5
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
